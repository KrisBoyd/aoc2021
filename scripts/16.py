from scripts.utility import read_data
from functools import reduce


def puzzles(data):
    """
    Decoding
    """
    s = data[0]
    # Hex to Bit
    packets = bin(int('F' + s, 16)).replace('0b1111', '')

    # PACKETS
    print(packets)
    find_packets(packets)
    print(version_sum)
    print(res)

    for k, v in res.items():
        print(k, v)

    # Evaluate res
    tree = res.copy()

    new_tree = tree.copy()
    # First do literals
    for k, v in tree.items():
        if k == 's1':
            continue
        if v['operation'] == 'literal':
            new_tree[v['parent']]['value'].append(v['value'])
            del new_tree[k]
        else:
            new_tree[v['parent']]['value'].append(k)

    # Then do operations until complete
    stop = False
    while not stop:
        tree = new_tree.copy()
        for k, v in tree.items():
            if all([type(b) is int for b in v['value']]):
                if v['operation'] == 'sum':
                    value = sum(v['value'])
                elif v['operation'] == 'product':
                    value = reduce((lambda x, y: x * y), v['value'])
                elif v['operation'] == 'minimum':
                    value = min(v['value'])
                elif v['operation'] == 'maximum':
                    value = max(v['value'])
                elif v['operation'] == 'greater':
                    value = int(v['value'][0] > v['value'][1])
                elif v['operation'] == 'lesser':
                    value = int(v['value'][0] < v['value'][1])
                elif v['operation'] == 'equal':
                    value = int(v['value'][0] == v['value'][1])

                if k == 's1':
                    print(value)
                    stop = True
                parent_value = new_tree[v['parent']]['value']
                parent_value = [p for p in parent_value if p != k]
                parent_value += [value]
                new_tree[v['parent']]['value'] = parent_value
                del new_tree[k]


version_sum = 0
res = {}
me = 0


value_dict = {
    0: 'sum',
    1: 'product',
    2: 'minimum',
    3: 'maximum',
    5: 'greater',
    6: 'lesser',
    7: 'equal',
}


def find_packets(s, parent=0):
    global me
    global res
    global version_sum
    me += 1

    res[f's{me}'] = {'parent': f's{parent}'}
    # print(res)
    # print(version_sum)
    v = int(s[0:3], 2)
    version_sum += v

    t = int(s[3:6], 2)
    if t != 4:
        res[f's{me}']['operation'] = value_dict[t]
        res[f's{me}']['value'] = []

        i = int(s[6], 2)
        if i == 0:
            l = int(s[7:22], 2)
            subpackets = s[22:(22+l)]
            parent_loop = me
            res[f's{me}']['length'] = l
            while len(subpackets) > 0:
                subpackets = find_packets(subpackets, parent=parent_loop)
        else:
            n = int(s[7:18], 2)
            subpackets = s[18:]
            parent_loop = me
            res[f's{me}']['n'] = n
            for i in range(n):
                subpackets = find_packets(subpackets, parent=parent_loop)
    else:

        # j = 1
        # literal_value = 0
        # position = 1
        # while j > 0:
        #     position += 5
        #     bits = s[(position):(position+5)]
        #     if int(bits[0]) == 0:
        #         j = 0
        #     literal_value += int(bits[1:], 2)

        literal_value, subpackets = get_literal_value(s[6:])
        print(literal_value)
        res[f's{me}']['value'] = literal_value
        res[f's{me}']['operation'] = 'literal'
        # subpackets = s[(position+5):]

    return subpackets


import numpy as np
def get_literal_value(packet):
    bits = [packet[i:i + 5] for i in range(0, len(packet), 5)]
    bits = bits[:np.where([b.startswith('0') for b in bits])[0][0] + 1]
    packet = packet[sum(len(b) for b in bits):]
    return int(''.join([b[1:] for b in bits]), 2), packet


if __name__ == '__main__':





    # Read Data
    day = __file__.split('/')[-1].split('.')[0]
    data = read_data(f'data/{day}.txt', integer=False)

    # Do puzzles
    puzzles(data)
