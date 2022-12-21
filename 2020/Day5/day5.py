def get_seat_id(seat):
    row = [i for i in range(128)]
    col = [i for i in range(8)]
    for char in seat:
        if char == 'F':
            row = row[:len(row) // 2]
        elif char == 'B':
            row = row[len(row) // 2:]
        elif char == "L":
            col = col[:len(col) // 2]
        elif char == "R":
            col = col[len(col) // 2:]
    return (row[0] * 8) + col[0]


def part1(file_name):
    file = open(file_name, 'r')
    max_id = -1
    for line in file:
        line = line.strip()
        seat_id = get_seat_id(line)
        if seat_id > max_id:
            max_id = seat_id
    return max_id


def part2(file_name):
    file = open(file_name, 'r')
    ids = []
    for line in file:
        line = line.strip()
        seat_id = get_seat_id(line)
        ids.append(seat_id)
    ids.sort()
    my_seat = []
    for i in range(len(ids) - 1):
        if ids[i] + 1 != ids[i + 1]:
            if ids[i] + 2 == ids[i + 1]:
                my_seat.append(ids[i] + 1)
    return my_seat


def main():
    file_name = "Part1Input.txt"
    print(part2(file_name))


if __name__ == '__main__':
    main()
