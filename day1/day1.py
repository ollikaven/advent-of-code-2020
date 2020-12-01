from itertools import combinations

with open("input.txt") as f:
    content = f.readlines()

numbers = [int(x.strip()) for x in content]

target_number = 2020

solutions = [pair for pair in combinations(
    numbers, 2) if sum(pair) == target_number]
print(f"Solutions: {solutions}")
m = solutions[0][0] * solutions[0][1]
print(f"Multiple: {m}")

solutions = [trio for trio in combinations(
    numbers, 3) if sum(trio) == target_number]
print(f"Solutions: {solutions}")
m = solutions[0][0] * solutions[0][1] * solutions[0][2]
print(f"Multiple: {m}")
