from scripts.utility import read_data


def find_neighbours(df, i, j):
    len_i = len(df)
    len_j = len(df[0])

    nb = [[i-1, j-1], [i, j-1], [i+1, j-1],
          [i-1, j],             [i+1, j],
          [i-1, j+1], [i, j+1], [i+1, j+1]]

    # remove invalid
    remove = []
    if i == 0:
        remove += [0, 3, 5]
    elif (i + 1) == len_i:
        remove += [2, 4, 7]
    if j == 0:
        remove += [0, 1, 2]
    elif (j + 1) == len_j:
        remove += [5, 6, 7]

    if len(remove):
        nb = [s for a, s in enumerate(nb) if a not in remove]

    return nb


def puzzles(data):
    """
    Flashing
    """
    df = []
    for y in data:
       df += [[int(x) for x in y]]

    flashes = 0
    steps = 0
    while True:  # for n in range(100): # for part 1
        steps += 1
        flashing = []
        # +1
        for y in range(len(df)):
            for x in range(len(df[0])):
                df[y][x] += 1
                if df[y][x] == 10:
                    flashing += [[x, y]]

        while flashing:
            i, j = flashing.pop(0)
            print((i, j))
            nb = find_neighbours(df, i, j)
            for x, y in nb:
                df[y][x] += 1
                if df[y][x] == 10:
                    flashing += [[x, y]]

        # reset flashes & count
        flashes = 0  # comment for part 1
        for y in range(len(df)):
            for x in range(len(df[0])):
                if df[y][x] >= 10:
                    df[y][x] = 0
                    flashes += 1

        # For part 2
        if flashes == 100:
            print(steps)
            break


if __name__ == '__main__':
    # Read Data
    day = __file__.split('/')[-1].split('.')[0]
    data = read_data(f'data/{day}.txt', integer=False)

    # Do puzzles
    puzzles(data)
