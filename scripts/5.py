from scripts.utility import read_data


def create_map(data, straight_only=False):
    n = 1000
    seamap = [[0] * n for _ in range(n)]

    for line in data:
        line = [int(s) for s in line]
        x0, y0, x1, y1 = line

        if x0 == x1:
            top = max(y0, y1)
            bottom = min(y0, y1)
            y_line = [top - s for s in range(top-bottom)] + [bottom]
            for y in y_line:
                seamap[x0][y] += 1
        elif y0 == y1:
            top = max(x0, x1)
            bottom = min(x0, x1)
            x_line = [top - s for s in range(top-bottom)] + [bottom]
            for x in x_line:
                seamap[x][y0] += 1
        else:
            # Diagonal
            if straight_only:
                continue

            length = abs(x0-x1) + 1
            sign_x = [-1 if (x0 - x1) > 0 else 1][0]
            sign_y = [-1 if (y0 - y1) > 0 else 1][0]

            x_line = [x0 + sign_x * s for s in range(length)]
            y_line = [y0 + sign_y * s for s in range(length)]

            for x, y in zip(x_line, y_line):
                seamap[x][y] += 1

    return seamap


def puzzle_one(data):
    """
    Find seamap of lines
    """
    seamap = create_map(data, straight_only=True)

    n_points = 0
    for x_row in seamap:
        n_points += sum([y >= 2 for y in x_row])

    print(f'Solution = {n_points}')


def puzzle_two(data):
    """
    Find losing bingo card
    """
    seamap = create_map(data, straight_only=False)

    n_points = 0
    for x_row in seamap:
        n_points += sum([y >= 2 for y in x_row])

    print(f'Solution = {n_points}')


if __name__ == '__main__':
    # Read Data
    day = __file__.split('/')[-1].split('.')[0]
    data = read_data(f'data/{day}.txt', integer=False)

    data = [s.replace(' -> ', ',') for s in data]
    data = [s.split(',') for s in data]

    # Do puzzles
    puzzle_one(data)
    puzzle_two(data)
