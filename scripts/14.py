from scripts.utility import read_data


def puzzles(data):
    """
    Polymer
    """
    start = data[0]
    instructions = data[2:]
    instructions = {s.split(' -> ')[0]: s.split(' -> ')[1] for s in instructions}

    # Initialize dict of pairs
    pairs = {}
    for i in range(len(start)-1):
        key = start[i] + start[i+1]
        if key in pairs:
            pairs[key] += 1
        else:
            pairs[key] = 1

    chars = {s: start.count(s) for s in set(start)}

    for i in range(40):
        new_pairs = {k: 0 for k in instructions}
        for k, v in pairs.items():
            if v > 0:
                new = k[0] + instructions[k], instructions[k] + k[1]
                new_pairs[new[0]] += v
                new_pairs[new[1]] += v
                chars[instructions[k]] += v
        pairs = new_pairs.copy()

    # max - min
    print(max(chars.values()) - min(chars.values()))




if __name__ == '__main__':
    # Read Data
    day = __file__.split('/')[-1].split('.')[0]
    data = read_data(f'data/{day}.txt', integer=False)

    # Do puzzles
    puzzles(data)
