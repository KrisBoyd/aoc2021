from scripts.utility import read_data


def puzzles(data):
    """
    Folding
    """
    idx = data.index('')
    df = data[:idx]
    df = [[int(s.split(',')[0]), int(s.split(',')[1])] for s in df]

    instructions = data[(idx+1):]
    instructions = [i.replace('fold along ', '') for i in instructions]

    for ins in instructions:
        c, v = ins.split('=')
        v = int(v)

        # Fold !
        if c == 'y':
            for s in df:
                if s[1] > v:
                    s[1] = v - (s[1] - v)
        elif c == 'x':
            for s in df:
                if s[0] > v:
                    s[0] = v - (s[0] - v)

        df = [list(s) for s in list(set([tuple(s) for s in df]))]
        print(len(df))

    # Visualize df
    import matplotlib.pyplot as plt

    for s in df:
        plt.plot(s[0], -s[1], marker='o', markersize=10, markerfacecolor='blue')
    plt.gca().set_aspect('equal')
    plt.show()
    plt.close('all')


if __name__ == '__main__':
    # Read Data
    day = __file__.split('/')[-1].split('.')[0]
    data = read_data(f'data/{day}.txt', integer=False)

    # Do puzzles
    puzzles(data)
