
def read_input(file_name):
    file = open(file_name, 'r')
    rules = {}
    my_ticket = []
    nearby_tickets = []
    reading = "rules"
    for line in file:
        line = line.strip()
        if line == "":
            continue
        elif line == "your ticket:":
            reading = "your ticket"
            continue
        elif line == "nearby tickets:":
            reading = "nearby tickets"
            continue
        if reading == "rules":
            rule = line.split(':')
            rule_class = rule[0]
            bounds = [bound.strip().split('-') for bound in rule[1].split("or")]
            for i in range(len(bounds)):
                bounds[i] = (int(bounds[i][0]), int(bounds[i][1]))
            rules[rule_class] = bounds
        elif reading == "your ticket":
            my_ticket = [int(val) for val in line.split(',')]
        elif reading == "nearby tickets":
            nearby_tickets.append([int(val) for val in line.split(',')])
    return rules, my_ticket, nearby_tickets


def part2(rules, nearby_tickets, my_ticket):
    num_classes = len(rules.keys())
    good_tickets = []
    for ticket in nearby_tickets:
        tic = []
        for val in ticket:
            possible_cats = []
            valid = False
            for key in rules.keys():
                rule = rules.get(key)
                if rule[0][0] <= val <= rule[0][1] or rule[1][0] <= val <= rule[1][1]:
                    valid = True
                    possible_cats.append(key)

            if not valid:
                break
            else:
                tic.append(set(possible_cats))
        if len(tic) == num_classes:
            good_tickets.append(tic)
    correct_order = []
    for i in range(num_classes):
        possibilities = good_tickets[0][i]
        for j in range(len(good_tickets)):
            possibilities = possibilities.intersection(good_tickets[j][i])
            if len(possibilities) == 1:
                break
        correct_order.append(list(possibilities))


    placed_classes = []
    while len(placed_classes) != 20:
        removed_class = ""
        for i in range(num_classes):
            if len(correct_order[i]) == 1 and correct_order[i][0] not in placed_classes:
                removed_class = correct_order[i][0]
                placed_classes.append(removed_class)
                break
        for i in range(num_classes):
            if removed_class in correct_order[i] and len(correct_order[i]) != 1:
                correct_order[i].remove(removed_class)
    for i in range(len(correct_order)):
        correct_order[i] = correct_order[i][0]
    keys = ["departure location", "departure station", "departure platform", "departure track", "departure date", "departure time"]
    total = 1
    for key in keys:
        ind = correct_order.index(key)
        total *= my_ticket[ind]
    return total


def part1(rules, nearby_tickets):
    invalid = []
    for ticket in nearby_tickets:
        for val in ticket:
            valid = False
            for rule in rules.values():
                if rule[0][0] <= val <= rule[0][1] or rule[1][0] <= val <= rule[1][1]:
                    valid = True
                    break
            if not valid:
                invalid.append(val)
    total_invalid = 0
    for val in invalid:
        total_invalid += val
    return total_invalid


def main():
    file_name = "Part1Input.txt"
    rules, my_ticket, nearby_tickets = read_input(file_name)
    print(part1(rules, nearby_tickets))
    print(part2(rules, nearby_tickets, my_ticket))


if __name__ == '__main__':
    main()
