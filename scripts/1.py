from scripts.utility import read_data


def puzzle_one(data):
    increase, decrease, flat = (0, 0, 0)

    previous = data[0]
    for current in data[1:]:
        if current > previous:
            increase += 1
        elif current < previous:
            decrease += 1
        else:
            flat += 1
        previous = current

    print(f'Number of increases = {increase}')


def puzzle_two(data):
    increase, decrease, flat = (0, 0, 0)

    previous = [data[0], data[1], data[2]]
    for i in range(len(data) - 3):
        i += 1
        current = [data[i], data[i+1], data[i+2]]

        if sum(current) > sum(previous):
            increase += 1
        elif sum(current) < sum(previous):
            decrease += 1
        else:
            flat += 1
        previous = current

    print(f'Number of increases = {increase}')


if __name__ == '__main__':
    # Read Data
    day = __file__.split('/')[-1].split('.')[0]
    data = read_data(f'data/{day}.txt', integer=True)

    # Puzzles
    sum([(a < b) for a, b in zip(data[:-1], data[1:])])
    sum([(a < b) for a, b in zip(data[:-3], data[3:])])

    # Do puzzles
    puzzle_one(data)
    puzzle_two(data)
