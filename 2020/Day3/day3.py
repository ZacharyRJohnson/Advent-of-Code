def process_input(file_name):
    file = open(file_name)
    tree_map = []
    for line in file:
        line = line.replace('\n', '')
        tree_map.append([char for char in line])
    return tree_map


def part1(tree_map):
    row = 0
    col = 0
    trees_encountered = 0
    while row < len(tree_map)-1:
        row += 1
        col = (col + 3) % len(tree_map[0])
        if tree_map[row][col] == '#':
            trees_encountered += 1
    return trees_encountered


def part2(tree_map, slopes):
    trees_seen = []
    for slope in slopes:
        row = 0
        col = 0
        trees_encountered = 0
        while row < len(tree_map)-1:
            row += slope[0]
            col = (col + slope[1]) % len(tree_map[0])
            if tree_map[row][col] == '#':
                trees_encountered += 1
        trees_seen.append(trees_encountered)
    final_val = 1
    for num in trees_seen:
        final_val *= num
    return final_val


def main():
    file_name = "Part1Input.txt"
    tree_map = process_input(file_name)
    print(part1(tree_map))
    slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    print(part2(tree_map, slopes))


if __name__ == '__main__':
    main()
