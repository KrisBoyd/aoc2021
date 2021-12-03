import pandas as pd
from scripts.utility import read_data


def puzzle_one(data):
    """
    forward X increases the horizontal position by X units.
    down X increases the depth by X units.
    up X decreases the depth by X units.
    """
    x = 0  # horizontal
    y = 0  # depth

    for c in data:
        if c[0] == 'forward':
            x += int(c[1])
        elif c[0] == 'down':
            y += int(c[1])
        elif c[0] == 'up':
            y -= int(c[1])

    print(f'Final depth = {y}')
    print(f'Final horizontal = {x}')
    print(f'Product {x*y}')


def puzzle_two(data):
    """
    down X increases your aim by X units.
    up X decreases your aim by X units.
    forward X does two things:
        It increases your horizontal position by X units.
        It increases your depth by your aim multiplied by X.
    """
    x = 0  # horizontal
    y = 0  # depth
    aim = 0

    for c in data:
        if c[0] == 'forward':
            x += int(c[1])
            y += aim * int(c[1])
        elif c[0] == 'down':
            aim += int(c[1])
        elif c[0] == 'up':
            aim -= int(c[1])

    print(f'Final depth = {y}')
    print(f'Final horizontal = {x}')
    print(f'Product {x * y}')


if __name__ == '__main__':
    # Read Data
    day = __file__.split('/')[-1].split('.')[0]
    data = read_data(f'data/{day}.txt', integer=False)
    data = [s.split(' ') for s in data]

    # Do puzzles
    puzzle_one(data)
    puzzle_two(data)
