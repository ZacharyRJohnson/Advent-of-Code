
def read_input(file_name):
    file = open(file_name, 'r')
    nums = []
    for line in file:
        line = int(line.strip())
        nums.append(line)
    return nums


def part1(preamble_len, nums):
    for i in range(preamble_len, len(nums)):
        num = nums[i]
        preamble = nums[i-preamble_len:i]
        valid = False
        for j in range(preamble_len):
            dif = num - preamble[j]
            if dif in (preamble[0:j] + preamble[j+1:preamble_len]):
                valid = True
                break
        if not valid:
            return num


def sum_list(nums):
    total = 0
    for num in nums:
        total += num
    return total


def part2(nums, inv_num):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sub_list = nums[i:j+1]
            sum_sub_list = sum_list(sub_list)
            if sum_sub_list == inv_num:
                return min(sub_list) + max(sub_list)
            elif sum_sub_list > inv_num:
                break


def main():
    file = "Part1Input.txt"
    preamble_len = 25
    nums = read_input(file)
    inv_num = part1(preamble_len, nums)
    print(inv_num)
    print(part2(nums, inv_num))


if __name__ == '__main__':
    main()
