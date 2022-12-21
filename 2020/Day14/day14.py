
def read_input(file_name):
    file = open(file_name, 'r')
    instructions = []
    for line in file:
        line = line.strip()
        inst = [x.strip() for x in line.split('=')]
        instructions.append(tuple(inst))
    return instructions


def apply_mask(mask, val):
    for i in range(len(mask)):
        if mask[i] == "X":
            continue
        else:
            val = val[:i] + mask[i] + val[i+1:]
    return val


def apply_mem_mask(mask, mem_adr):
    floaters = []
    for i in range(len(mask)):
        if mask[i] == "0":
            continue
        elif mask[i] == "1":
            mem_adr = mem_adr[:i] + mask[i] + mem_adr[i+1:]
        else:
            floaters.append(i)
    floating_adrs = []
    for i in range(pow(2, len(floaters))):
        bin_val = bin(i)[2:]
        temp = mem_adr
        offset = 0
        for ind, f_ind in enumerate(floaters):
            if (len(floaters) - 1) - ind >= len(bin_val):
                temp = temp[:f_ind] + '0' + temp[f_ind + 1:]
                offset += 1
            else:
                temp = temp[:f_ind] + bin_val[ind - offset] + temp[f_ind + 1:]
        floating_adrs.append(temp)
    return floating_adrs


def part1(instructions):
    mask = ""
    mem = ["" for i in range(100000)]
    for inst in instructions:
        if inst[0] == "mask":
            mask = inst[1]
        else:
            mem_adr = int(inst[0][4:-1])
            val = format(int(inst[1]), '#038b')[2:]
            m_val = apply_mask(mask, val)
            mem[mem_adr] = m_val
    total = 0
    for val in mem:
        if val != "":
            total += int(val, 2)
    return total


def part2(instructions):
    mask = ""
    mem = {}
    for inst in instructions:
        if inst[0] == "mask":
            mask = inst[1]
        else:
            mem_adr = format(int(inst[0][4:-1]), '#038b')[2:]
            val = int(inst[1])
            mem_adrs = apply_mem_mask(mask, mem_adr)
            for adr in mem_adrs:
                mem[int(adr, 2)] = val
    total = 0
    for val in mem.values():
        if val != "":
            total += int(val)
    return total


def main():
    file_name = "Part1Input.txt"
    instructions = read_input(file_name)
    print(part1(instructions))
    print(part2(instructions))

if __name__ == '__main__':
    main()
