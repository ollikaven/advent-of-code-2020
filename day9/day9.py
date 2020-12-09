from itertools import combinations

with open("day9/input.txt", "r") as file:
    _input = [int(x.strip()) for x in file.readlines()]


def is_sum(numbers, target_number):
    solutions = [pair for pair in combinations(
        numbers, 2) if sum(pair) == target_number]
    if len(solutions) > 0:
        return True
    else:
        return False


def find_weakness(series, preamble):
    numbers = series[0:preamble]
    for n in series[preamble:]:
        if not is_sum(numbers, n):
            return n
        numbers.pop(0)
        numbers.append(n)


def consecutive(L, n):
    for i in range(len(L)+1):
        for j in range(i+1, len(L)+1):
            s = sum(L[i:j])
            if s == n:
                return L[i:j]
            elif s > n:
                break

    return []


result = find_weakness(_input, 25)
print(f"0901: {result}")

series = consecutive(_input, result)
res = min(series) + max(series)
print(f"0902: {res}")
