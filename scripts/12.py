from scripts.utility import read_data


small_cave = (False, '')

def puzzles(data):
    """
    Pathfinding
    """
    df = [s.split('-') for s in data]

    # Create network
    m = {}
    for a in df:
        if a[0] not in m:
            m[a[0]] = []
        m[a[0]].append(a[1])
        if a[1] not in m:
            m[a[1]] = []
        m[a[1]].append(a[0])

    path = []
    def travel(m, pos, current_path):
        global small_cave
        for x in m[pos]:
            print(x)
            if x == 'start':
                continue
            if x.islower() and x in current_path:
                if small_cave[0] is False:
                    small_cave = (True, x)
                    current_path.append(x)
                    travel(m, pos=x, current_path=current_path)
                continue
            elif x == 'end':
                final_path = current_path + [x]
                path.append([final_path])
            else:
                current_path.append(x)
                travel(m, pos=x, current_path=current_path)
        if current_path.pop() == small_cave[1]:
            small_cave = (False, "")

    travel(m, 'start', ['start'])

    print(len(path))


if __name__ == '__main__':
    # Read Data
    day = __file__.split('/')[-1].split('.')[0]
    data = read_data(f'data/{day}.txt', integer=False)

    # Do puzzles
    puzzles(data)
