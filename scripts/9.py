from scripts.utility import read_data


def puzzle_one(data):
    """
    Map; low points
    """
    risk_level_sum = 0
    for i, y in enumerate(data):
        row = [int(s) for s in list(y[0])]
        for j, x in enumerate(row):
            surrounding = []
            if i < len(data) - 1:
                surrounding += [int(list(data[i+1][0])[j])]
            if i > 0:
                surrounding += [int(list(data[i-1][0])[j])]
            if j < len(row) - 1:
                surrounding += [int(list(data[i][0])[j+1])]
            if j > 0:
                surrounding += [int(list(data[i][0])[j-1])]
            if sum([x >= s for s in surrounding]) == 0:
                risk_level_sum += (1 + x)
    print(risk_level_sum)


def puzzle_two(data):
    """
    Find 3 largest basins
    """
    for i, r in enumerate(data):
        data[i] = [int(s) for s in list(r[0])]

    current_basin = 0
    grouped_basins = {}
    for i, y in enumerate(data):
        for j, x in enumerate(y):
            if x == 9:
                continue
            if i > 0:
                up = data[i-1][j]
            else:
                up = 9
            if j > 0:
                left = data[i][j-1]
            else:
                left = 9

            if (up == 9) and (left == 9):
                current_basin -= 1
                data[i][j] = current_basin
            elif (up == 9) and (left < 0):
                data[i][j] = left
            elif (up < 0) and (left == 9):
                data[i][j] = up
            elif (up < 0) and (left < 0):
                data[i][j] = max(up, left)
                if up != left:
                    if max(up, left) in grouped_basins:
                        grouped_basins[max(up, left)] = list(set(grouped_basins[max(up, left)] + [min(up, left)]))
                    else:
                        grouped_basins[max(up, left)] = [min(up, left)]

    # Group basins that are adjacent to each other
    new_groups = {}
    for k, v in grouped_basins.items():
        for g in new_groups.items():
            if k in g[1]:
                new_groups[g[0]] += v
                break
        else:
            new_groups[k] = v
    groups = [[k] + v for k, v in new_groups.items()]
    groups = [list(set(s)) for s in groups]

    all_groups = [-s-1 for s in range(-min([min(i) for i in data]))]
    groups += [[s] for s in list(set(all_groups) - set([i for s in groups for i in s]))]

    # Get size of Basins
    basins = {}
    for g in groups:
        value = 0
        for b in g:
            value += sum([b == s for r in data for s in r])
        basins[str(g)] = value

    largest = sorted(list(basins.values()), reverse=True)[0:3]
    print(largest)
    print(f'{largest[0] * largest[1] * largest[2]}')


if __name__ == '__main__':
    # Read Data
    day = __file__.split('/')[-1].split('.')[0]
    data = read_data(f'data/{day}.txt', integer=False)
    data = [s.split(' ') for s in data]

    # Do puzzles
    puzzle_one(data)
    puzzle_two(data)
