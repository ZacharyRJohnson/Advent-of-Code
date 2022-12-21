
def read_input(file_name):
    file = open(file_name, 'r')
    bag_rules = {}
    for line in file:
        line = line.strip()
        line = line.replace(".", "")
        split_line = [x.strip() for x in line.split("contain")]
        top_bag = split_line[0]
        if "bags" in top_bag:
            top_bag = top_bag.replace("bags", "").strip()
        elif "bag" in top_bag:
            top_bag = top_bag.replace("bag", "").strip()
        sub_bags = [x.strip() for x in split_line[1].split(',')]
        for i in range(len(sub_bags)):
            sub_bag = sub_bags[i]
            if "bags" in sub_bag:
                sub_bag = sub_bag.replace("bags", "").strip()
            elif "bag" in sub_bag:
                sub_bag = sub_bag.replace("bag", "").strip()
            if sub_bag == "no other":
                sub_bag = (0, "")
            else:
                sub_bag = (int(sub_bag[0]), sub_bag[2:])
            sub_bags[i] = sub_bag
        bag_rules[top_bag] = sub_bags
    return bag_rules


def part1(bag_rules):
    can_hold_gold = []
    for key in bag_rules:
        sub_bags = [rule[1] for rule in bag_rules[key]]
        for bag in sub_bags:
            if bag == "shiny gold":
                can_hold_gold.append(key)
                break
            elif bag in can_hold_gold:
                can_hold_gold.append(key)
                break
            elif recurse_bags(bag_rules, bag):
                can_hold_gold.append(key)
                break
    return len(can_hold_gold)


def recurse_bags(bag_rules, bag):
    if bag == "shiny gold":
        return 1
    elif bag == "":
        return 0
    total = 0
    for rule in bag_rules[bag]:
        total += recurse_bags(bag_rules, rule[1])
    return 1 if total > 0 else 0


def part2(bag_rules):
    gold_rules = bag_rules["shiny gold"]
    total = 0
    for rule in gold_rules:
        total += recurse_count(bag_rules, rule[1], rule[0])
    return total


def recurse_count(bag_rules, bag, num_bags):
    total = num_bags
    for rule in bag_rules[bag]:
        if rule[1] == "":
            return num_bags
        total += num_bags * recurse_count(bag_rules, rule[1], rule[0])
    return total


def main():
    file = "Part1Input.txt"
    bag_rules = read_input(file)
    print(part1(bag_rules))
    print(part2(bag_rules))


if __name__ == '__main__':
    main()
