import pandas as pd


def read_data(loc, integer=True):
    with open(loc) as f:
        data = f.readlines()
    data = [s.replace('\n', '') for s in data]

    if integer:
        data = [int(s) for s in data]

    return data
