from scripts.utility import read_data


def puzzle_one(data):
    """
    Decoding
    """
    n = 0
    for entry in data:
        entry = entry[-4:]
        for s in entry:
            if len(s) in [2, 3, 4, 7]:
                n += 1
    print(n)


def puzzle_two(data):
    """
    """
    total_value = 0
    for entry in data:
        input = entry[:-5]
        output = entry[-4:]

        mapping = {}

        # Map 1, 4, 7 & 8
        map_unique = {2: 1, 3: 7, 4: 4, 7: 8}
        # Identify 1, 4, 7 & 8
        for s in input:
            if len(s) in list(map_unique.keys()):
                mapping[map_unique[len(s)]] = s

        # Identify 2, 3 & 5:
        # Both 5 long, 2 has 2 matches with 4, 3 & 5 have 3 matches with 4.
        for s in input:
            if len(s) == 5:
                intersect = set(s).intersection(mapping[4])
                if len(intersect) == 2:
                    mapping[2] = s
                elif len(intersect) == 3:
                    # 3 has two matches with 1, 5 only one
                    intersect = set(s).intersection(mapping[1])
                    if len(intersect) == 1:
                        mapping[5] = s
                    elif len(intersect) == 2:
                        mapping[3] = s

        # Identify 0, 6 & 9: All length 6.
        for s in input:
            if len(s) == 6:
                # 6: only one match with 1
                if len(set(s).intersection(mapping[1])) == 1:
                    mapping[6] = s
                # 9: exactly 4 & 5 combined
                elif set(s) == set(mapping[4]).union(mapping[5]):
                   mapping[9] = s
                # 0
                else:
                    mapping[0] = s

        # Find output value
        digits = []
        for digit in output:
            for k, v in mapping.items():
                if set(v) == set(digit):
                    digits += [k]
        value = sum([s * 10 ** (len(digits) - i - 1) for i, s in enumerate(digits)])
        total_value += value

    print(total_value)


if __name__ == '__main__':
    # Read Data
    day = __file__.split('/')[-1].split('.')[0]
    data = read_data(f'data/{day}.txt', integer=False)
    data = [s.split(' ') for s in data]

    # Do puzzles
    puzzle_one(data)
    puzzle_two(data)
