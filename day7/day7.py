rules = {}
with open("day7/input.txt", "r") as file:
    for line in file.readlines():
        k, v = line[:-2].split(" contain ")
        k = k.rsplit(" ", 1)[0]
        rules[k] = {}

        for bag in v.split(", "):
            if bag != "no other bags":
                parts = bag.split(" ")
                rules[k][' '.join(parts[1:3])] = int(parts[0])


def can_contain(bag, start):
    if bag == start:
        return True
    else:
        return any(can_contain(x, start) for x in rules[bag])


total = sum([can_contain(bag, "shiny gold")
             for bag in rules if bag != "shiny gold"])
print(f"0701: {total}")


def count_bags(bag):
    return 1 + sum(count_bags(inner_bag) * n for inner_bag, n in rules[bag].items())


total = count_bags("shiny gold") - 1
print(f"0702: {total}")
