import re


def format_input(input_file):
    with open(input_file, 'r') as file:
        _input = file.read()

    _input = [x.replace("\n", " ") for x in _input.split("\n\n")]
    _input = [x.split(" ") for x in _input]

    final_input = []
    for passport in _input:
        e = {}
        for field in passport:
            if len(field) > 0:
                s = field.split(":")
                e[s[0]] = s[1]
        final_input.append(e)
    return final_input


def has_fields(passport):
    if {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"} <= passport.keys():
        return True
    else:
        return False


def valid_byr(passport):
    byr = passport["byr"]
    if byr.isdigit() and 1920 <= int(byr) <= 2002:
        return True
    else:
        return False


def valid_iyr(passport):
    val = passport["iyr"]
    if val.isdigit() and 2010 <= int(val) <= 2020:
        return True
    else:
        return False


def valid_eyr(passport):
    val = passport["eyr"]
    if val.isdigit() and 2020 <= int(val) <= 2030:
        return True
    else:
        return False


def valid_hgt(passport):
    val = passport["hgt"]
    valid = False
    if val[-2:] == "cm":
        if 150 <= int(val[:-2]) <= 193:
            valid = True
    elif val[-2:] == "in":
        if 59 <= int(val[:-2]) <= 76:
            valid = True
    return valid


def valid_hcl(passport):
    val = passport["hcl"]
    if re.match(r"^#[0-9a-f]{6}", val):
        return True
    else:
        return False


def valid_pid(passport):
    val = passport["pid"]
    if re.match(r"^[0-9]{9}$", val):
        return True
    else:
        return False


def valid_ecl(passport):
    val = passport["ecl"]
    if val in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
        return True
    else:
        return False


def valid_passport(passport):
    if (has_fields(passport)
            and valid_byr(passport)
            and valid_iyr(passport)
            and valid_eyr(passport)
            and valid_hgt(passport)
            and valid_hcl(passport)
            and valid_ecl(passport)
            and valid_pid(passport)):
        return True
    else:
        return False


# Part 1
_input = format_input("day4/input.txt")
valid_passports = 0
for passport in _input:
    if has_fields(passport):
        valid_passports += 1
print(valid_passports)


# Part 2
valid_passports = 0
for passport in _input:
    if valid_passport(passport):
        valid_passports += 1
print(valid_passports)
