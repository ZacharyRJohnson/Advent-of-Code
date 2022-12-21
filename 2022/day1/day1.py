def get_input(file):
    file = open(file, 'r')
    inputNums = []
    totCals = 0
    for line in file:
        line = line.strip()
        if line == "":
            inputNums.append(totCals)
            totCals = 0
            continue
        totCals += int(line)
    return inputNums

def part1(input):
    return max(input)

def part2(input):
    input.sort(reverse=True)
    return input[0] + input[1] + input[2]

def main():
    in1 = "in1.txt"
    in2 = "in2.txt"
    input = get_input(in1)
    print(part1(input))
    print(part2(input))

if __name__ == '__main__':
    main()
