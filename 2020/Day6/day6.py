
def part1(file_name):
    file = open(file_name, 'r')
    total_yes = 0
    group = ""
    for line in file:
        line = line.strip()
        if line == "\n" or line == "":
            total_yes += len(list(dict.fromkeys([c for c in group])))
            group = ""
        else:
            group += line
    total_yes += len(list(dict.fromkeys([c for c in group])))
    return total_yes


def part2(file_name):
    file = open(file_name, 'r')
    everyone_yes = 0
    group = []
    for line in file:
        line = line.strip()
        if line == "\n" or line == "":
            m_set = set(group[0])
            for person in group[1:]:
                m_set = m_set & set(person)
            everyone_yes += len(m_set)
            group = []
        else:
            group.append([c for c in line])
    m_set = set(group[0])
    for person in group[1:]:
        m_set = m_set & set(person)
    everyone_yes += len(m_set)
    return everyone_yes


def main():
    file_name = "Part1Input.txt"
    print(part1(file_name))
    print(part2(file_name))


if __name__ == '__main__':
    main()
