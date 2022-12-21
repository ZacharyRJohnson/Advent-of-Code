import re


def part1(fileName):
    valid_pwds = 0
    file = open(fileName, 'r')
    for line in file:
        line_comp = line.split(':')
        pwd = line_comp[1].replace('\n', '')
        rules = line_comp[0].split(" ")
        special_char = rules[1]
        split_range = rules[0].split('-')
        minimum = int(split_range[0])
        maximum = int(split_range[1])
        processed_pwd = re.sub('[^' + special_char + ']*', '', pwd)
        if minimum <= len(processed_pwd) <= maximum:
            valid_pwds += 1
    return valid_pwds


def part2(fileName):
    valid_pwds = 0
    file = open(fileName, 'r')
    for line in file:
        line_comp = line.split(':')
        pwd = line_comp[1].replace('\n', '')
        rules = line_comp[0].split(" ")
        special_char = rules[1]
        split_range = rules[0].split('-')
        first_ind = int(split_range[0])
        second_ind = int(split_range[1])
        # No zero indexing for some reason, very confused
        if (pwd[first_ind] == special_char and pwd[second_ind] != special_char) or (pwd[first_ind] != special_char and pwd[second_ind] == special_char):
            valid_pwds += 1
    return valid_pwds


def main():
    print(part1("Part1Input.txt"))
    print(part2("Part1Input.txt"))


if __name__ == '__main__':
    main()
