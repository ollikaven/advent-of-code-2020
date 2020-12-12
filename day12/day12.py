with open("day12/input.txt", "r") as file:
    _input = [x.strip() for x in file.readlines()]


def angle_to_direction(angle):
    return angle / 90 % 4


def location(move, s):
    global direction
    action = move[0]
    steps = int(move[1:])
    if action == "N":
        return [s[0], s[1]+steps]
    elif action == "S":
        return [s[0], s[1]-steps]
    elif action == "W":
        return [s[0]-steps, s[1]]
    elif action == "E":
        return [s[0]+steps, s[1]]
    elif action == "F":
        if direction == 0.0:
            return [s[0], s[1]+steps]
        elif direction == 2.0:
            return [s[0], s[1]-steps]
        elif direction == 3.0:
            return [s[0]-steps, s[1]]
        elif direction == 1.0:
            return [s[0]+steps, s[1]]
    elif action == "L":
        direction = (direction - angle_to_direction(steps)) % 4
        return s
    elif action == "R":
        direction = (direction + angle_to_direction(steps)) % 4
        return s
    else:
        return s


def manhattan_distance(location):
    return sum([abs(x) for x in location])


direction = 1.0
s = [0, 0]
for ins in _input:
    s = location(ins, s)
md = manhattan_distance(s)
print(f"1201: {md}")


ship = [0, 0]
waypoint = [10, 1]
for move in _input:
    action = move[0]
    steps = int(move[1:])
    if action == "N":
        waypoint = [waypoint[0], waypoint[1]+steps]
    elif action == "S":
        waypoint = [waypoint[0], waypoint[1]-steps]
    elif action == "W":
        waypoint = [waypoint[0]-steps, waypoint[1]]
    elif action == "E":
        waypoint = [waypoint[0]+steps, waypoint[1]]
    elif action == "F":
        forward = [steps*x for x in waypoint]
        ship = [ship[0]+forward[0], ship[1]+forward[1]]
    elif action == "R":
        if steps == 90:
            waypoint = [waypoint[1], -waypoint[0]]
        elif steps == 180:
            waypoint = [-waypoint[0], -waypoint[1]]
        else:
            waypoint = [-waypoint[1], waypoint[0]]
    elif action == "L":
        if steps == 90:
            waypoint = [-waypoint[1], waypoint[0]]
        elif steps == 180:
            waypoint = [-waypoint[0], -waypoint[1]]
        else:
            waypoint = [waypoint[1], -waypoint[0]]
md = manhattan_distance(ship)
print(f"1202: {md}")
