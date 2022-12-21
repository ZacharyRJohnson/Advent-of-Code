
def read_input(file_name):
    file = open(file_name, 'r')
    depart_time = int(file.readline().strip())
    id_string = file.readline().strip().split(',')
    bus_ids = []
    for r_id in id_string:
        bus_ids.append(r_id)
    return depart_time, bus_ids


def part1(latest_depart, buses):
    min_bus = (0, 1000000000)
    for b_id in buses:
        if b_id == 'x':
            continue
        b_id = int(b_id)
        time_to_next_depart = b_id * ((latest_depart // b_id) + 1) - latest_depart
        if min_bus[1] > time_to_next_depart:
            min_bus = (b_id, time_to_next_depart)
    return min_bus[0] * min_bus[1]


def slow_part2(buses):
    first_id = int(buses[0])
    counter = first_id
    while True:
        w_count = counter + 1
        for i in range(1, len(buses)):
            if buses[i] == 'x':
                w_count += 1
            elif w_count % int(buses[i]) == 0:
                w_count += 1
                if i == len(buses) - 1:
                    return counter
            else:
                break
        counter += first_id


def part2(buses):
    time = 0
    step = 1
    p2 = [(int(i), j) for j, i in enumerate(buses) if i != 'x']
    for bus_id, minutes in p2:
        while(time + minutes) % bus_id != 0:
            time += step
        step *= bus_id
    return time


def main():
    file_name = "Part1Input.txt"
    depart_time, bus_ids = read_input(file_name)
    print(part1(depart_time, bus_ids))
    print(part2(bus_ids))


if __name__ == '__main__':
    main()
