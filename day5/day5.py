with open('day5/input.txt', 'r') as file:
    _input = [x.strip() for x in file.readlines()]


def locate(s, n, boarding_pass):
    if len(s) == 1:
        return s[0]
    else:
        if boarding_pass[n] in ("F", "L"):
            return locate(s[:len(s)//2], n+1, boarding_pass)
        else:
            return locate(s[len(s)//2:], n+1, boarding_pass)


def seat_id(boading_pass):
    row = locate(list(range(0, 128)), 0, boading_pass)
    seat = locate(list(range(0, 8)), 7, boading_pass)
    seat_id = row * 8 + seat
    return seat_id


a = []
for line in _input:
    s_id = seat_id(line)
    a.append(s_id)

# Part 1
max_seat_id = max(a)
print(max_seat_id)

# Part 2
a.sort()
b = [x for x in range(a[0], a[-1] + 1)]
a = set(a)
b = set(b)
print(list(a ^ b))
