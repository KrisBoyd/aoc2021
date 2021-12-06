from scripts.utility import read_data


def puzzle_one(data, days=80):
    """
    Simulate lantern fish growth
    """
    state_0 = {s: data.count(s) for s in range(9)}

    fish = []
    fish += [(sum(state_0.values()), state_0)]

    state = state_0
    for day in range(days):
        # decrease timer
        state = {(k-1): v for k, v in state.items()}

        # add babies
        state[6] += state[-1]
        state[8] = state[-1]
        del state[-1]

        # save current state
        fish += [(sum(state.values()), state)]

    print(f'fish = {fish[-1][0]}')


def puzzle_two(data):
    """
    Lantern fishies after 256 days
    """
    puzzle_one(data, days=256)


if __name__ == '__main__':
    # Read Data
    day = __file__.split('/')[-1].split('.')[0]
    data = read_data(f'data/{day}.txt', integer=False)
    data = [int(s) for s in data[0].split(',')]

    # Do puzzles
    puzzle_one(data)
    puzzle_two(data)
