from scripts.utility import read_data


def puzzles(data):
    """
    Beaconing
    """
    scanners = {}
    for s in data:
        if s == '':
            continue
        if 'scanner' in s:
            v = int(s.split('scanner ')[1].split(' ')[0])
            scanners[v] = []
        else:
            scanners[v].append([int(i) for i in s.split(',')])

    # Part 1
    def find_distances(scanner):
        distances = {}
        for i, (x1, y1, z1) in enumerate(scanner):
            distances[i] = []
            for j, (x2, y2, z2) in enumerate(scanner):
                if i == j:
                    continue
                distance = (x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2
                distances[i].append(distance)
        return distances

    # Check if we can discover overlapping distances of 11!
    def find_pairs(distances0, distances1, scanner0, scanner1):
        pairs = []
        for beacon0, dist0 in distances0.items():
            for beacon1, dist1 in distances1.items():
                if len(set(dist0).intersection(set(dist1))) >= 11:
                    pairs.append([scanner0[beacon0], scanner1[beacon1]])
        return pairs

    # Find orientation
    def find_orient(pairs, c0):
        p0, p1 = pairs[0]
        for c in [0, 1, 2]:  # Try x, y, z
            for orient in [-1, 1]:
                diff = p0[c0] - orient * p1[c]
                if all([p[0][c0] - orient * p[1][c] == diff for p in pairs[1:]]):
                    return orient, c, diff

    def solve_next_scanner(solved_scanners, unsolved_scanners):
        for scanner0 in solved_scanners.values():
            distances0 = find_distances(scanner0)
            for u, scanner1 in unsolved_scanners.items():
                distances1 = find_distances(scanner1)
                pairs = find_pairs(distances0, distances1, scanner0, scanner1)
                if len(pairs) >= 12:
                    orient = {}
                    for c0 in [0, 1, 2]:
                        orient[c0] = find_orient(pairs, c0)

                    # Apply orient to current scanner to solve it
                    rotated_scanner, location = apply_orient(scanner1, orient)
                    print(f'Solved scanner {u} at location {location}')
                    return u, rotated_scanner, location

    def apply_orient(scanner, orient):
        rotated_scanner = [[0 for i in s] for s in scanner]
        for c in [0, 1, 2]:  # x, y, z
            for i in range(len(rotated_scanner)):
                rotated_scanner[i][c] = scanner[i][orient[c][1]] * orient[c][0] + orient[c][2]

        location = (orient[0][2], orient[1][2], orient[2][2])

        return rotated_scanner, location

    # Part 1
    coordinates = {}
    coordinates[0] = (0, 0, 0)
    solved = {}
    solved[0] = scanners[0]
    unsolved = {k: v for k, v in scanners.items() if k != 0}

    while len(unsolved) > 0:
        u, new, location = solve_next_scanner(solved, unsolved)
        solved[u] = new
        unsolved = {k: v for k, v in unsolved.items() if k != u}
        coordinates[u] = location

    beacons = []
    for k, v in solved.items():
        beacons += [tuple(s) for s in v]
    print(f'Number of beacons = {len(set(beacons))}')

    # Part 2
    max_distance = 0
    for i, d_i in coordinates.items():
        for j, d_j in coordinates.items():
            if i == j:
                continue
            else:
                max_distance = max(max_distance, sum([abs(a-b) for a, b in zip(d_i, d_j)]))
    print(f'Maximum distance = {max_distance}')


if __name__ == '__main__':
    # Read Data
    day = __file__.split('/')[-1].split('.')[0]
    data = read_data(f'data/{day}.txt', integer=False)

    # Do puzzles
    puzzles(data)
