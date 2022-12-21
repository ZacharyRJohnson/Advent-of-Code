def read_input(file_name):
    file = open(file_name, 'r')
    layout = []
    for line in file:
        line = line.strip()
        row = [c for c in line]
        layout.append(row)
    return layout


def occupied_adj_seats(layout, i, j):
    num_occupied = 0
    for x in range(max(0, i-1), min(len(layout), i+2)):
        for y in range(max(0, j-1), min(len(layout[0]), j+2)):
            if x == i and y == j:
                continue
            if layout[x][y] == '#':
                num_occupied += 1
    return num_occupied


def check_los(layout, i, j):
    num_occupied = 0
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0,  -1),          (0,  1),
                  (1,  -1), (1,  0), (1,  1)]
    for direction in directions:
        x = i + direction[0]
        y = j + direction[1]
        while 0 <= x < len(layout) and 0 <= y < len(layout[0]):
            if layout[x][y] == '#':
                num_occupied += 1
                break
            if layout[x][y] == 'L':
                break
            x += direction[0]
            y += direction[1]
    return num_occupied


def part1(layout):
    changed = True
    while changed:
        new_layout = []
        changed = False
        for i in range(len(layout)):
            row = []
            for j in range(len(layout[0])):
                if layout[i][j] == '.':
                    row.append('.')
                    continue
                num_occupied = occupied_adj_seats(layout, i, j)
                if layout[i][j] == 'L' and num_occupied == 0:
                    row.append('#')
                    changed = True
                elif layout[i][j] == '#' and num_occupied >= 4:
                    row.append('L')
                    changed = True
                else:
                    row.append(layout[i][j])
            new_layout.append(row)
        layout = new_layout
    total_oc = 0
    for i in range(len(layout)):
        total_oc += layout[i].count('#')
    return total_oc


def part2(layout):
    changed = True
    while changed:
        new_layout = []
        changed = False
        for i in range(len(layout)):
            row = []
            for j in range(len(layout[0])):
                if layout[i][j] == '.':
                    row.append('.')
                    continue
                num_occupied = check_los(layout, i, j)
                if layout[i][j] == 'L' and num_occupied == 0:
                    row.append('#')
                    changed = True
                elif layout[i][j] == '#' and num_occupied >= 5:
                    row.append('L')
                    changed = True
                else:
                    row.append(layout[i][j])
            new_layout.append(row)
        layout = new_layout
    total_oc = 0
    for i in range(len(layout)):
        total_oc += layout[i].count('#')
    return total_oc


def main():
    file_name = "Part1Input.txt"
    layout = read_input(file_name)
    print(part1(layout))
    print(part2(layout))


if __name__ == '__main__':
    main()
