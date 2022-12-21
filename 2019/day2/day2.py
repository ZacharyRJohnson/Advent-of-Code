def fillMemory(file):
    memory = []
    with open(file) as f:
        for line in f:
            memory += [int(n) for n in line.strip().split(",")]
    return memory

def compute(memory):
    for i in range(0, len(memory), 4):
        op = memory[i]
        if(op == 99):
            return memory
        arg1 = memory[memory[i+1]]
        arg2 = memory[memory[i+2]]
        returnPos = memory[i+3]

        if(op == 1):
            memory[returnPos] = arg1 + arg2
        elif(op == 2):
            memory[returnPos] = arg1 * arg2
        else:
            print("Error reading opcode at: " + i)
            print("Opcode: " + memory[i])
            return memory
    
def main():
    memory = fillMemory("input1.txt")
    memory = compute(memory)
    print(memory[0])

main()