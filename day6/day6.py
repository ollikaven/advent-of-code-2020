with open('day6/input.txt', 'r') as file:
    _input = [x.strip() for x in file.readlines()]


groups = [[]]
for i in _input:
    if not i:
        groups.append([])
    else:
        groups[-1].append(i)

# Part 1
result = ["".join(x) for x in groups]
total = sum(list(map(lambda x: len(set(x)), result)))
print(f"0601: {total}")

# Part 2
total = 0
for i, group in enumerate(result):
    res = {i: group.count(i) for i in set(group)}
    g_member_count = len(groups[i])
    same_answers = sum(value == g_member_count for value in res.values())
    total += same_answers
print(f"0602: {total}")
