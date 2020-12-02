import pandas as pd

input = pd.read_csv("day2/input.txt", header=None)

new = input[0].str.split(" ", expand=True)
reqs = new[0].str.split("-", expand=True)
min = reqs[0].astype("int64")
max = reqs[1].astype("int64")
c = new[1].str.get(0)
pwd = new[2]

frame = {"min": min, "max": max, "c": c, "pwd": pwd}
df = pd.DataFrame(frame)


# Part 1
valid_pwds = 0
for index, row in df.iterrows():
    occurances = row["pwd"].count(row["c"])
    if row["min"] <= occurances <= row["max"]:
        valid_pwds += 1

# Part 2
valid_pwds = 0
for index, row in df.iterrows():
    indeces_to_access = []
    indeces_to_access.append(row["min"] - 1)
    indeces_to_access.append(row["max"] - 1)
    accessed_mapping = map(row["pwd"].__getitem__, indeces_to_access)
    accessed_list = list(accessed_mapping)
    cnt = accessed_list.count(row["c"])
    if cnt == 1:
        valid_pwds += 1
