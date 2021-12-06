from scripts.utility import read_data


def BINGO(draws, cards):
    filled_cards = cards.copy()
    for d in draws:
        for i_c, c in enumerate(cards):
            for i_r, r in enumerate(c):
                for i_i, i in enumerate(r):
                    if i == d:
                        filled_cards[i_c][i_r][i_i] = -1
        # Check rows or columns for completion
        for i_c, c in enumerate(filled_cards):
            cols = [0] * len(c[0])
            for i_r, r in enumerate(c):
                if sum(r) == -5:
                    print(f'Card {i_c} - {c} is the winner!')
                    return d, c
                cols = [a + b for a, b in zip(cols, r)]
                if -5 in cols:
                    print(f'Card {i_c} - {c} is the winner!')
                    return d, c


def puzzle_one(draws, cards):
    """
    Find winning bingo card
    """
    final_draw, card = BINGO(draws, cards)

    sum_unmarked = 0
    for r in card:
        for i in r:
            if i != -1:
                sum_unmarked += i

    print(f'Solution = {final_draw * sum_unmarked}')


def ANTIBINGO(draws, cards):
    filled_cards = cards.copy()
    incomplete_cards = range(len(filled_cards))

    for d in draws:
        for i_c, c in enumerate(cards):
            for i_r, r in enumerate(c):
                for i_i, i in enumerate(r):
                    if i == d:
                        filled_cards[i_c][i_r][i_i] = -1
        # Check rows or columns for completion
        for i_c, c in enumerate(filled_cards):
            cols = [0] * len(c[0])
            for i_r, r in enumerate(c):
                if sum(r) == -5:
                    print(f'Card {i_c} is completed!')
                    incomplete_cards = set(incomplete_cards) - {i_c}
                cols = [a + b for a, b in zip(cols, r)]
                if -5 in cols:
                    print(f'Card {i_c} is completed!')
                    incomplete_cards = set(incomplete_cards) - {i_c}

                if len(incomplete_cards) == 0:
                    return d, c


def puzzle_two(draws, cards):
    """
    Find losing bingo card
    """
    final_draw, card = ANTIBINGO(draws, cards)

    sum_unmarked = 0
    for r in card:
        for i in r:
            if i != -1:
                sum_unmarked += i

    print(f'Solution = {final_draw * sum_unmarked}')


if __name__ == '__main__':
    # Read Data
    day = __file__.split('/')[-1].split('.')[0]
    data = read_data(f'data/{day}.txt', integer=False)

    draws = [int(s) for s in data[0].split(',')]
    cards = [[]]
    i = 0
    for s in data[2:]:
        if s == '':
            i += 1
            cards += [[]]
        else:
            cards[i] += [[int(p) for p in s.strip(' ').replace('  ', ' ').split(' ')]]

    # Do puzzles
    puzzle_one(draws, cards)
    puzzle_two(draws, cards)
