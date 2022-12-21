
def read_input(file_name):
    file = open(file_name, 'r')
    instructions = []
    for line in file:
        line = line.strip()
        inst = (line[0], int(line[1:]))
        instructions.append(inst)
    return instructions


def part1(instructions):
    cords = {'N': 0, 'S': 0, 'E': 0, 'W': 0}
    facing = 0
    directions = {0: 'E', 90: "S", 180: "W", 270: "N"}
    for inst in instructions:
        cur_facing = directions[facing]
        if inst[0] == 'N':
            cords['N'] += inst[1]
        elif inst[0] == 'S':
            cords['S'] += inst[1]
        elif inst[0] == 'E':
            cords['E'] += inst[1]
        elif inst[0] == 'W':
            cords['W'] += inst[1]
        elif inst[0] == 'L':
            facing = (facing - inst[1]) % 360
        elif inst[0] == 'R':
            facing = (facing + inst[1]) % 360
        elif inst[0] == 'F':
            cords[cur_facing] += inst[1]
    return abs(cords['N'] - cords['S']) + abs(cords['E'] - cords['W'])


def rotate(waypoint, times):
    keys = list(waypoint.keys())
    values = list(waypoint.values())
    values = values[times:] + values[:times]
    return dict(zip(keys, values))


def part2(instructions):
    cords = {'N': 0, 'S': 0, 'E': 0, 'W': 0}
    waypoint = {'N': 1, 'E': 10, 'S': 0, 'W': 0}
    for inst in instructions:
        if inst[0] == 'N':
            waypoint['N'] += inst[1]
        elif inst[0] == 'S':
            waypoint['S'] += inst[1]
        elif inst[0] == 'E':
            waypoint['E'] += inst[1]
        elif inst[0] == 'W':
            waypoint['W'] += inst[1]
        elif inst[0] == 'L':
            times = inst[1] // 90
            waypoint = rotate(waypoint, times)
        elif inst[0] == 'R':
            times = -(inst[1] // 90)
            waypoint = rotate(waypoint, times)
        elif inst[0] == 'F':
            for key in cords.keys():
                cords[key] += waypoint[key] * inst[1]
    return abs(cords['N'] - cords['S']) + abs(cords['E'] - cords['W'])


def main():
    file_name = "Part1Input.txt"
    instructions = read_input(file_name)
    print(part1(instructions))
    print(part2(instructions))


if __name__ == '__main__':
    main()
