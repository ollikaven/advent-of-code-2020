from collections import defaultdict

with open("day10/input.txt", "r") as file:
    _input = [int(x.strip()) for x in file.readlines()]
    _input.sort()


diffs = defaultdict(int)
diffs[3] = 1
arr = defaultdict(int)
arr[0] = 1
prev = 0

for adapter in _input:
    diffs[adapter - prev] += 1
    arr[adapter] = arr[adapter-1] + arr[adapter-2] + arr[adapter-3]
    prev = adapter

total_diffs = diffs[1] * diffs[3]
print(f"1001: {total_diffs}")
max_arr = arr[max(arr)]
print(f"1002: {max_arr}")
