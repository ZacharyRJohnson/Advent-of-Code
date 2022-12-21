
def read_input(file_name):
    file = open(file_name, 'r')
    nums = []
    for line in file:
        line = line.strip()
        nums.append(int(line))
    return nums


def part1(nums):
    nums.sort()
    one_j_dif = 0
    three_j_dif = 0
    for i in range(len(nums)):
        j_dif = 0
        if i == 0:
            j_dif = nums[0]
        else:
            j_dif = nums[i] - nums[i-1]
        if j_dif == 1:
            one_j_dif += 1
        elif j_dif == 3:
            three_j_dif += 1
    three_j_dif += 1  # For the built in adapter
    return three_j_dif * one_j_dif


def main():
    file_name = "Part1Input.txt"
    nums = read_input(file_name)
    print(part1(nums))


if __name__ == '__main__':
    main()
