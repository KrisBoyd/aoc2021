from scripts.utility import read_data

def add(x, y):
    return f'[{x},{y}]'


def explode(s, idx):
    idx_end = s.index(']', idx)  # find sublist end
    c = s.index(',', idx)  # find comma index

    n1 = int(s[(idx+1):c])
    n2 = int(s[(c+1):s.index(']', c)])

    # find left
    for j in range(idx):
        if s[(idx-j)].isnumeric():
            left = int(s[(idx-j)])
            left_idx = idx-j
            if s[(idx-j-1)].isnumeric():  # check for 2 digit numbers
                left = int(s[idx-j-1:idx-j+1])
            break
    else:
        left = -1
        left_idx = idx

    # find right
    r = c + len(str(n2)) + 2  # comma; n_2; ]; , or [
    for j in range(len(s[r:])):
        if s[r+j].isnumeric():
            right = int(s[r+j])
            right_idx = r+j
            if s[r+j+1].isnumeric():  # check for 2 digit numbers
                right = int(s[r+j:r+j+2])
            break
    else:
        right = -1
        right_idx = len(s)-1

    s1 = list(s)
    # replace sublist with 0
    for i in range(idx, idx_end+1):
        if i == idx:
            s1[i] = '0'
        else:
            s1[i] = ''

    # Increase values
    if right >= 0:
        s1[right_idx] = str(right + n2)
        if right >= 10:
            s1[right_idx+1] = ''
    if left >= 0:
        s1[left_idx] = str(left + n1)
        if left >= 10:
            s1[left_idx-1] = ''

    s1 = ''.join(s1)
    return s1


def split(s, idx):
    n = int(s[idx:(idx+2)])
    n1 = n // 2
    n2 = n - n1

    s1 = list(s)
    s1[idx] = ''
    s1[idx+1] = f'[{n1},{n2}]'

    s1 = ''.join(s1)

    return s1


def magnitude(s):
    s1 = list(s)
    for idx, v in enumerate(s):
        if v == ']':
            _idx = s[:idx].rindex('[') + 1
            pair = eval(s[_idx-1:idx+1])
            m = pair[0]*3 + pair[1]*2

            # Update list
            s1[_idx-1] = str(m)
            for r in range(_idx, idx+1):
                s1[r] = ''
            s1 = ''.join(s1)
            return magnitude(s1)
    return int(s)


def red(s):
    brackets = 0
    for i, v in enumerate(s):
        if v == '[':
            brackets += 1
            if brackets == 5:
                s = explode(s, i)
                return red(s)
        elif v == ']':
            brackets -= 1
    for i, v in enumerate(s):
        if v.isnumeric() and s[i+1].isnumeric():
            s = split(s, i)
            return red(s)
    return s


def puzzles(data):
    """
    Decoding
    """
    # Part 1
    start = data[0]
    for x in data[1:]:
        start = add(start, x)
        start = red(start)
    print(magnitude(start))

    # Part 2
    max_magnitude = 0
    for i, x in enumerate(data):
        for j, y in enumerate(data):
            if i == j:
                continue
            max_magnitude = max(max_magnitude, magnitude(red(add(x, y))))
    print(max_magnitude)





if __name__ == '__main__':
    # Read Data
    day = __file__.split('/')[-1].split('.')[0]
    data = read_data(f'data/{day}.txt', integer=False)

    # Do puzzles
    puzzles(data)
