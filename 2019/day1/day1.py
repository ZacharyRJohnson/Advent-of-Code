def calcFuel(mass):
    return (mass//3) - 2

def calcFuel2(mass):
    fuel = (mass//3) - 2
    if(fuel < 0):
        return 0
    return fuel + calcFuel2(fuel)

def main():
    sum1 = 0
    sum2 = 0
    with open("input1.txt") as f:
        for line in f:
            line = line.strip()
            sum1 += calcFuel(int(line))
            sum2 += calcFuel2(int(line))
    print("Part 1 answer: " + str(sum1))
    print("Part 2 answer: " + str(sum2))

main()