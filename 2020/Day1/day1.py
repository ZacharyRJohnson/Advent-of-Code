def getInput(fileName):
    file = open(fileName, 'r')
    inputNums = []
    for line in file:
        inputNums.append(int(line))
    return inputNums


def part1(input):
    for i in range(len(input) - 2):
        for j in range((i+1), len(input) - 1):
            if (input[i] + input[j]) == 2020:
                return input[i] * input[j]


def part2(input):
    for i in range(len(input) - 3):
        for j in range((i+1), len(input) - 2):
            for k in range((j+1), len(input) - 1):
                if (input[i] + input[j] + input[k]) == 2020:
                    return input[i] * input[j] * input[k]


def main():
    file1 = "Part1Input.txt"
    inputNums = getInput(file1)
    print("Part1 answer: " + str(part1(inputNums)))
    print("Part2 answer: " + str(part2(inputNums)))


if __name__ == '__main__':
    main()
