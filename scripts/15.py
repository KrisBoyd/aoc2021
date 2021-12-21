from scripts.utility import read_data


def puzzles(data):
    """
    Pathfinding
    """
    # Travel around
    def solve(grid):
        costs = [[float('inf')] * len(grid) for s in range(len(grid))]
        costs[0][0] = 0

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        n = len(grid)
        while True:
            old_cost = sum([sum(s) for s in costs])
            print(old_cost)
            for i in range(len(grid)):
                for j in range(len(grid)):
                    price = costs[i][j]

                    # look around
                    for dir in directions:
                        x = i + dir[0]
                        y = j + dir[1]

                        if (x >= 0) and (y >= 0) and (x < n) and (y < n):
                            price = min(price, costs[x][y] + grid[i][j])

                    costs[i][j] = price
            if old_cost == sum([sum(s) for s in costs]):
                break
        return costs[n-1][n-1]

    # part 1
    grid_1 = [[int(y) for y in x] for x in data]
    print(solve(grid_1))

    # part 2
    n = len(grid_1)

    grid_2 = [[0] * n * 5 for s in range(n*5)]
    for i in range(5):
        for j in range(5):
            chunk = grid_1.copy()
            for t in range(i+j):
                chunk = [[(y % 9 + 1) for y in x] for x in chunk]

            for ii, row in enumerate(chunk):
                for jj, v in enumerate(row):
                    grid_2[i * n + ii][j * n + jj] = v

    print(solve(grid_2))


if __name__ == '__main__':
    # Read Data
    day = __file__.split('/')[-1].split('.')[0]
    data = read_data(f'data/{day}.txt', integer=False)

    # Do puzzles
    puzzles(data)
