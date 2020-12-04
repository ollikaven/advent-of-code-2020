import pytest

from day4 import day4 as day

invalid_input = day.format_input("day4/invalid_passports.txt")
valid_input = day.format_input("day4/valid_passports.txt")
test_input = day.format_input("day4/test_input.txt")


def test_has_fields():
    assert True == day.has_fields(test_input[0])
    assert False == day.has_fields(test_input[1])


def test_byr():
    assert True == day.valid_byr({"byr": "2000"})
    assert True == day.valid_byr({"byr": "2002"})
    assert False == day.valid_byr({"byr": "1919"})
    assert False == day.valid_byr({"byr": "20cb02"})


def test_iyr():
    assert True == day.valid_iyr({"iyr": "2015"})
    assert True == day.valid_iyr({"iyr": "2010"})
    assert False == day.valid_iyr({"iyr": "2000"})
    assert False == day.valid_iyr({"iyr": "dssdg2000"})


def test_eyr():
    assert True == day.valid_eyr({"eyr": "2020"})
    assert True == day.valid_eyr({"eyr": "2030"})
    assert False == day.valid_eyr({"eyr": "20200"})
    assert False == day.valid_eyr({"eyr": "202fdgfd00"})


def test_hgt():
    assert True == day.valid_hgt({"hgt": "193cm"})
    assert True == day.valid_hgt({"hgt": "60in"})
    assert False == day.valid_hgt({"hgt": "60"})
    assert False == day.valid_hgt({"hgt": "250cm"})


def test_hcl():
    assert True == day.valid_hcl({"hcl": "#123abc"})
    assert False == day.valid_hcl({"hcl": "#123abg"})
    assert False == day.valid_hcl({"hcl": "123abg"})


def test_ecl():
    assert True == day.valid_ecl({"ecl": "blu"})
    assert False == day.valid_ecl({"ecl": "blsdgdsu"})
    assert False == day.valid_ecl({"ecl": "ogl"})


def test_pid():
    assert True == day.valid_pid({"pid": "000000000"})
    assert False == day.valid_pid({"pid": "0123456789"})


def test_valid_passport():
    assert True == day.valid_passport(valid_input[0])
    assert False == day.valid_passport(invalid_input[0])
