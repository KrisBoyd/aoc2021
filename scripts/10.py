from scripts.utility import read_data


def simplify(line):
    pairs = {'{': '}',
             '[': ']',
             '(': ')',
             '<': '>'}

    i = 0
    idx_remove = []
    while i < (len(line) - 1):
        a = line[i]
        b = line[i + 1]
        if a in pairs and pairs[a] == b:
            idx_remove += [i, i + 1]
            i += 1
        elif a in pairs and b in pairs.values():
            print(f'Expected {pairs[a]}, but found {b} instead')
            return b
        i += 1
    new_line = ''.join([c for j, c in enumerate(list(line)) if j not in idx_remove])
    if len(line) != len(new_line):
        return simplify(new_line)
    else:
        return new_line


def puzzles(data):
    """
    Navigation
    """
    res = []
    for s in data:
        res += [simplify(s)]

    scoring = {')': 3,
               ']': 57,
               '}': 1197,
               '>': 25137}
    print(sum([scoring[s] for s in res if len(s) == 1]))

    # Puzzle 2: discard corrupted lines
    res = [r for r in res if len(r) > 1]

    # Complete the lines
    pairs = {'{': '}',
             '[': ']',
             '(': ')',
             '<': '>'}
    values = {')': 1,
              ']': 2,
              '}': 3,
              '>': 4}

    completed = {}
    for r in res:
        a = ''
        score = 0
        for i in range(len(r)):
            j = len(r) - i - 1
            a += pairs[r[j]]

            score *= 5
            score += values[pairs[r[j]]]

        completed[a] = score

    # Result
    print(sorted(list(completed.values()))[(len(completed.values()) + 1) // 2 - 1])



if __name__ == '__main__':
    # Read Data
    day = __file__.split('/')[-1].split('.')[0]
    data = read_data(f'data/{day}.txt', integer=False)

    # Do puzzles
    puzzles(data)
