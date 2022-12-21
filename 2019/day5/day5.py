def fillMemory(file):
    memory = []
    with open(file) as f:
        for line in f:
            memory += [int(n) for n in line.strip().split(",")]
    return memory

def compute(memory):
    i = 0
    while i < len(memory):
        instruction = str(memory[i])
        op = int(instruction[-2:])
        pMode1 = int(instruction[-3]) if len(instruction) >= 3 else 0
        pMode2 = int(instruction[-4]) if len(instruction) >= 4 else 0
        pMode3 = int(instruction[-5]) if len(instruction) >= 5 else 0
        if(op == 99):
            return memory
        arg1 = memory[i+1]
        arg2 = memory[i+2]

        if(op == 1):
            val1 = memory[arg1] if pMode1 == 0 else arg1
            val2 = memory[arg2] if pMode2 == 0 else arg2
            returnPos = memory[i+3]
            memory[returnPos] = val1 + val2
            i += 4
        elif(op == 2):
            val1 = memory[arg1] if pMode1 == 0 else arg1
            val2 = memory[arg2] if pMode2 == 0 else arg2
            returnPos = memory[i+3]
            memory[returnPos] = val1 * val2
            i += 4
        elif(op == 3):
            memory[arg1] = int(input("$: "))
            i += 2
        elif(op == 4):
            val1 = memory[arg1] if pMode1 == 0 else arg1
            print(val1)
            i += 2
        elif(op == 5):
            val1 = memory[arg1] if pMode1 == 0 else arg1
            val2 = memory[arg2] if pMode2 == 0 else arg2
            if(val1 != 0):
                i = val2
            else:
                i += 3
        elif(op == 6):
            val1 = memory[arg1] if pMode1 == 0 else arg1
            val2 = memory[arg2] if pMode2 == 0 else arg2
            if(val1 == 0):
                i = val2
            else:
                i += 3
        elif(op == 7):
            val1 = memory[arg1] if pMode1 == 0 else arg1
            val2 = memory[arg2] if pMode2 == 0 else arg2
            returnPos = memory[i+3]
            if(val1 < val2):
                memory[returnPos] = 1
            else:
                memory[returnPos] = 0
            i += 4
        elif(op == 8):
            val1 = memory[arg1] if pMode1 == 0 else arg1
            val2 = memory[arg2] if pMode2 == 0 else arg2
            returnPos = memory[i+3]
            if(val1 == val2):
                memory[returnPos] = 1
            else:
                memory[returnPos] = 0
            i += 4
        else:
            print("Error reading opcode at: " + str(i))
            print("Opcode: " + str(memory[i]))
            return memory
    
def main():
    memory = fillMemory("input1.txt")
    memory = compute(memory)
    #print(memory)

main()