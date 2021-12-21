from scripts.utility import read_data
from functools import reduce


def puzzles(data):
    """
    Decoding
    """
    s = data[0]
    target = {'x': [32, 65], 'y': [-225, -177]}
    # target = {'x': [20, 30], 'y': [-10, -5]}

    def fire(v_x, v_y, target):
        start_x = v_x
        start_y = v_y
        x = 0
        y = 0
        y_max = 0
        while True:
            x += v_x
            y += v_y

            y_max = max(y_max, y)

            if v_x > 0:
                v_x -= 1
            elif v_x < 0:
                v_x += 1
            v_y -= 1

            if (x >= target['x'][0]) and (x <= target['x'][1]) and (y >= target['y'][0]) and (y <= target['y'][1]):
                print(f'Reached Target from {start_x}, {start_y} - max height {y_max}')
                return True, x, y, y_max
            elif x >= target['x'][1] or y <= target['y'][0]:
                y_max = 0
                return False, x, y, y_max

    # result = {'x': 0, 'y': 0, 'height': 0}
    # for x_val in range(1, 101):
    #     for y_val in range(1, 301):
    #         res = fire(x_val, y_val, target)
    #         if res[0]:
    #             if res[3] > result['height']:
    #                 result['x'] = x_val
    #                 result['y'] = y_val
    #                 result['height'] = res[3]
    # print(result)

    # Part 2
    result = 0
    for x_val in range(1, 66):
        for y_val in range(-225, 2001):
            res = fire(x_val, y_val, target)
            if res[0]:
                result += 1
    print(result)





if __name__ == '__main__':
    # Read Data
    day = __file__.split('/')[-1].split('.')[0]
    data = read_data(f'data/{day}.txt', integer=False)

    # Do puzzles
    puzzles(data)
