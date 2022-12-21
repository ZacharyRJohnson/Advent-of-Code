def part1():
    parens = input("Enter parens: ")
    #parens = "(())(((()("
    floor = 0
    for c in parens:
        if(c == "("):
            floor += 1
        elif(c == ")"):
            floor -= 1
        else:
            print("Not a paren, quiting")
            break
    print(floor)

def part2():
    parens = input("Enter parens: ")
    #parens = "(())(((()("
    floor = 0
    pos = 0
    while(floor != -1):
        if(parens[pos] == "("):
            floor += 1
            pos += 1
        elif(parens[pos] == ")"):
            floor -= 1
            pos += 1
        else:
            print("Not a paren, quiting")
            break
    print(pos)

part2()
