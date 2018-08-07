from random import sample
from itertools import product


def get_random_placement(height, width, k):
    placement = []
    random_per_row = int(k / height)
    for row in range(height):
        random_col = list(product([row], range(width)))
        placement.extend(sample(random_col, random_per_row))

    surplus = list(product(range(height), range(width)))
    placement.extend(sample(surplus, k - random_per_row * height))

    return placement
