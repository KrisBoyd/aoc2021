import pandas as pd
from scripts.utility import read_data


def puzzle_one(data):
    """
    Gamma rate: find most common bit
    Epsilon rate: find least common bit
    """
    count_ones = [0] * len(data[0])

    for i in data:
        list_i = [int(s) for s in list(i)]
        count_ones = [i + j for i, j in zip(count_ones, list_i)]

    gamma_rate = [int(s > len(data)/2) for s in count_ones]
    gamma_value = sum([s*2**(len(gamma_rate) - 1 - i) for i, s in enumerate(gamma_rate)])

    epsilon_rate = [int(s < len(data)/2) for s in count_ones]
    epsilon_value = sum([s*2**(len(epsilon_rate) - 1 - i) for i, s in enumerate(epsilon_rate)])

    print(f'Gamma rate = {gamma_rate}')
    print(f'Epsilon rate = {epsilon_rate}')

    print(f'Power consumption = {gamma_value * epsilon_value}')


def find_common_bit(data, value='gamma', position=0):
    count_ones = [0] * len(data[0])

    for i in data:
        list_i = [int(s) for s in list(i)]
        count_ones = [i + j for i, j in zip(count_ones, list_i)]

    if value == 'gamma':
        return [int(s >= len(data) / 2) for s in count_ones][position]
    if value == 'epsilon':
        return [int(s < len(data) / 2) for s in count_ones][position]


def puzzle_two(data):
    """
    Filter values to find the
    - Oxygen generator rating
    - CO2 scrubber rating
    """
    def find_rating(df, value, position=0):
        common_bit = find_common_bit(df, value=value, position=position)

        df_filtered = [s for s in df if int(list(s)[position]) == common_bit]

        if len(df_filtered) > 1:
            return find_rating(df_filtered, value=value, position=position+1)
        else:
            return df_filtered[0]

    oxygen_rating = [int(s) for s in list(find_rating(df=data.copy(), value='gamma'))]
    oxygen_value = sum([s*2**(len(oxygen_rating) - 1 - i) for i, s in enumerate(oxygen_rating)])

    CO2_rating = [int(s) for s in list(find_rating(df=data.copy(), value='epsilon'))]
    CO2_value = sum([s*2**(len(CO2_rating) - 1 - i) for i, s in enumerate(CO2_rating)])

    print(f'Oxygen = {oxygen_value}')
    print(f'CO2 = {CO2_value}')
    print(f'Product {oxygen_value * CO2_value}')


if __name__ == '__main__':
    # Read Data
    day = __file__.split('/')[-1].split('.')[0]
    data = read_data(f'data/{day}.txt', integer=False)

    # Example data
    # data = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']

    # Do puzzles
    puzzle_one(data)
    puzzle_two(data)
