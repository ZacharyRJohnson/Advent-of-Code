

def read_in_tape(file_name):
    file = open(file_name, 'r')
    tape = []
    for line in file:
        line = line.strip()
        tape.append(line)
    return tape


def part1(tape):
    seen_inst = []
    pc = 0
    acc = 0
    while True:
        if pc in seen_inst:
            return acc
        seen_inst.append(pc)
        split_inst = tape[pc].split()
        inst = split_inst[0]
        val = int(split_inst[1])
        if inst == "acc":
            acc += val
        if inst == "jmp":
            pc += val
        else:
            pc += 1


def part2(tape):
    seen_inst = []
    pc = 0
    acc = 0
    while True:
        if pc == len(tape):
            return True, acc
        seen_inst.append(pc)
        split_inst = tape[pc].split()
        inst = split_inst[0]
        val = int(split_inst[1])
        if inst == "acc":
            acc += val
            pc += 1
        elif inst == "jmp":
            branch_state = branch(tape, seen_inst, pc, acc, ["nop", split_inst[1]])
            if branch_state[0]:
                return branch_state[1]
            else:
                pc += val
        elif inst == "nop":
            branch_state = branch(tape, seen_inst, pc, acc, ["jmp", split_inst[1]])
            if branch_state[0]:
                return branch_state[1]
            else:
                pc += 1


def branch(tape, seen_inst, pc, acc, new_inst):
    if new_inst[0] == "jmp":
        pc += int(new_inst[1])
    else:
        pc += 1
    while True:
        if pc in seen_inst:
            return False, acc
        elif pc == len(tape):
            return True, acc
        seen_inst.append(pc)
        split_inst = tape[pc].split()
        inst = split_inst[0]
        val = int(split_inst[1])
        if inst == "acc":
            acc += val
        if inst == "jmp":
            pc += val
        else:
            pc += 1


def main():
    file = "Part1Input.txt"
    tape = read_in_tape(file)
    print(part1(tape))
    print(part2(tape))


if __name__ == '__main__':
    main()
