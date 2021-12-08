from scripts.utility import read_data


def puzzle_one(data):
    """
    Min distance
    """
    data = sorted(data)

    n = len(data) // 2
    median = [data[n], data[n-1]]

    for m in median:
        print(sum([abs(s-m) for s in data]))


def fuel_cost(n):
    # f = 0
    # for i in range(n):
    #     f += (i+1)
    # return f
    return n


def puzzle_two(data):
    """
    """
    data = sorted(data)
    n = len(data)
    mean = sum(data) / n

    means = [int(mean), int(mean) + 1]
    for m in means:
        print(sum([fuel_cost(abs(s-m)) for s in data]))

    # Actually calculating
    fuel = {}
    for i in range(max(data) + 1):
        if i % 100 == 0:
            print(i)
        fuel[i] = sum([fuel_cost(abs(s-i)) for s in data])

    import seaborn as sns
    import matplotlib.pyplot as plt
    ax = sns.scatterplot(x=fuel.keys(), y=fuel.values(), color='red')
    plt.title('Crab submarines')
    ax.set_ylabel('Fuel')
    ax.set_xlabel('Position')
    plt.show()



if __name__ == '__main__':
    # Read Data
    day = __file__.split('/')[-1].split('.')[0]
    data = read_data(f'data/{day}.txt', integer=False)
    data = [int(s) for s in data[0].split(',')]

    # Do puzzles
    puzzle_one(data)
    puzzle_two(data)
