from scripts.utility import read_data


def replace_(string, ring):
    if ring == '.':
        return string.replace('#', '.')
    if ring == '#':
        return string.replace('.', '#')


def puzzles(data):
    """
    Mapping
    """
    iea = data[0]
    image = data[2:]

    for iter in range(50):
        if iter == 0:
            ring = '.'
        elif iter > 0:
            if last_ring == '.':
                ring = iea[0]
            else:
                ring = iea[-1]
        last_ring = ring
        # Add one ring of `.`
        image = [f'{ring}{s}{ring}' for s in image]
        image = [replace_(image[0], ring)] + image + [replace_(image[0], ring)]
        new_image = [list(s) for s in image]
        for i in range(len(image)):
            if i == 0:
                top_row = replace_(image[i], ring)
            else:
                top_row = image[i-1]
            middle_row = image[i]
            if i == len(image) - 1:
                bottom_row = replace_(image[i], ring)
            else:
                bottom_row = image[i+1]
            for j in range(len(middle_row)):
                if j == 0:
                    top = ring + top_row[j:j+2]
                    middle = ring + middle_row[j:j+2]
                    bottom = ring + bottom_row[j:j+2]
                elif j == len(middle_row) - 1:
                    top = top_row[j-1:j+1] + ring
                    middle = middle_row[j-1:j+1] + ring
                    bottom = bottom_row[j-1:j+1] + ring
                else:
                    top = top_row[j-1:j+2]
                    middle = middle_row[j-1:j+2]
                    bottom = bottom_row[j-1:j+2]

                bin_code = top + middle + bottom
                bin_number = bin_code.replace('.', '0').replace('#', '1')
                n = int(bin_number, 2)
                new_image[i][j] = iea[n]
        image = [''.join(s) for s in new_image]
        print('-' * 104)
        [print(s) for s in image]
        print('-' * 104)
    print(f"Lit pixels = {sum([sum([x == '#' for x in list(s)]) for s in image])}")


if __name__ == '__main__':
    # Read Data
    day = __file__.split('/')[-1].split('.')[0]
    data = read_data(f'data/{day}.txt', integer=False)

    # Do puzzles
    puzzles(data)
