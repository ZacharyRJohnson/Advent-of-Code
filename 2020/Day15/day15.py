
def part1(starting_nums):
    spoken = {}
    for i in range(len(starting_nums)):
        spoken[starting_nums[i]] = [i + 1, 0]
    last_num = starting_nums[-1]
    for turn in range(len(starting_nums) + 1, 2021):
        if spoken.get(last_num)[1] == 0:
            new_num = 0
        else:
            last_said = spoken.get(last_num)
            new_num = last_said[0] - last_said[1]

        if new_num in spoken.keys():
            last_zero = spoken.get(new_num)
            spoken[new_num] = [turn, last_zero[0]]
        else:
            spoken[new_num] = [turn, 0]

        last_num = new_num
        if turn == 2020:
            return last_num


def part2(starting_nums):
    spoken = {}
    for i in range(len(starting_nums)):
        spoken[starting_nums[i]] = [i + 1, 0]
    last_num = starting_nums[-1]
    for turn in range(len(starting_nums) + 1, 30000001):
        if spoken.get(last_num)[1] == 0:
            new_num = 0
        else:
            last_said = spoken.get(last_num)
            new_num = last_said[0] - last_said[1]

        if new_num in spoken.keys():
            last_zero = spoken.get(new_num)
            spoken[new_num] = [turn, last_zero[0]]
        else:
            spoken[new_num] = [turn, 0]

        last_num = new_num
        if turn == 30000000:
            return last_num


def main():
    p = [1, 2, 16, 19, 18, 0]
    test1 = [0, 3, 6]
    test2 = [1, 3, 2]
    test3 = [2, 1, 3]
    test4 = [1, 2, 3]
    test5 = [2, 3, 1]
    print("--- Tests P1 ---")
    print(part1(test1))
    print(part1(test2))
    print(part1(test3))
    print(part1(test4))
    print(part1(test5))
    print("--- Part1 ---")
    print(part1(p))
    print("--- Part2 ---")
    print(part2(p))
    

if __name__ == '__main__':
    main()
