import re


def process_input(file_name):
    file = open(file_name, 'r')
    passports = []
    passport = ""
    line = ""
    for line in file:
        if line == "\n" or line == "":
            passport = passport.strip()
            processed_passport = passport.split(" ")
            processed_passport = [tuple(field.split(':')) for field in processed_passport]
            passports.append(processed_passport)
            passport = ""
        else:
            passport += line.replace("\n", "") + " "
    passport = passport.strip()
    processed_passport = passport.split(" ")
    processed_passport = [tuple(field.split(':')) for field in processed_passport]
    passports.append(processed_passport)
    return passports


def is_valid_fields(passport):
    valid = True
    for part in passport:
        if not valid:
            return valid
        field = part[0]
        value = part[1]
        if field == "byr":
            if not (1920 <= int(value) <= 2002):
                valid = False
        elif field == "iyr":
            if not (2010 <= int(value) <= 2020):
                valid = False
        elif field == "eyr":
            if not (2020 <= int(value) <= 2030):
                valid = False
        elif field == "hgt":
            if value[-2:] == "cm":
                if not 150 <= int(value[:-2]) <= 193:
                    valid = False
            elif value[-2:] == "in":
                if not 59 <= int(value[:-2]) <= 76:
                    valid = False
            else:
                valid = False
        elif field == "hcl":
            if not re.match("^#[0-9a-f]{6}$", value):
                valid = False
        elif field == "ecl":
            if value not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                valid = False
        elif field == "pid":
            if len(value) != 9:
                valid = False
    return valid


def part1(passports):
    valid_ports = 0
    for passport in passports:
        if len(passport) == 8:
            valid_ports += 1
        elif len(passport) == 7 and not any("cid" in field for field in passport):
            valid_ports += 1
    return valid_ports


def part2(passports):
    valid_ports = 0
    for passport in passports:
        if len(passport) == 8:
            if is_valid_fields(passport):
                valid_ports += 1
        elif len(passport) == 7 and not any("cid" in field for field in passport):
            if is_valid_fields(passport):
                valid_ports += 1
    return valid_ports


def main():
    file_name = "Part1Input.txt"
    p_input = process_input(file_name)
    print(part1(p_input))
    print(part2(p_input))


if __name__ == '__main__':
    main()
