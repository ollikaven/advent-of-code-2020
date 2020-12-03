import numpy
from itertools import cycle


def nth_term(iterable, n):
    """Returns the nth term of any iterable."""
    for i, x in enumerate(iterable):
        if i == n:
            return x


def traverse(x, y, input_file):
    trees = 0
    n = x
    with open(input_file) as f:
        for line_number, line in enumerate(f):
            if line_number == 0 or line_number % y != 0:
                continue
            line_stripped = line.strip()
            loc = nth_term(cycle(line_stripped), n)
            if loc == '#':
                trees += 1
            n += x
    return trees


# Part 1
assert traverse(7, 1, "day3/test_input.txt") == 4
traverse(3, 1, "day3/test_input.txt")


# Part 2
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
assert traverse(1, 2, "day3/test_input.txt") == 2
assert numpy.prod([traverse(x, y, "day3/test_input.txt")
                   for x, y in slopes]) == 336

numpy.prod([traverse(x, y, "day3/input.txt")
            for x, y in slopes])
