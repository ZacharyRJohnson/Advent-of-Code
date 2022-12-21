# Part1

def calculatePossiblities(low, high):
    pswds = 0
    for i in range(low, high):
        if(isPossibility(i)):
            pswds += 1
    return pswds

def isPossibility(num):
    strNum = str(num)
    for j in range(0, 5):
        if(strNum[j] == strNum[j+1]):
            break
        elif(j+1 == 5):
            return False
    
    for j in range(0, 5):
        if(int(strNum[j]) > int(strNum[j+1])):
            return False

    return True

# Part2

def calculatePossiblities2(low, high):
    pswds = 0
    for i in range(low, high):
        if(isPossibility2(i)):
            pswds += 1
    return pswds

def isPossibility2(num):
    strNum = str(num)
    j = 0
    while j < 5:
        if(strNum[j] == strNum[j+1]):
            if(j+2 < 6 and strNum[j] == strNum[j+2]):
                dupNum = strNum[j] 
                j += 2
                while j < 5 and strNum[j+1] == dupNum:
                    j += 1
            else:    
                break
        if(j+1 >= 5):
            return False
        j += 1
    
    for j in range(0, 5):
        if(int(strNum[j]) > int(strNum[j+1])):
            return False

    return True

#print(calculatePossiblities(130254, 678275))
print(calculatePossiblities2(130254, 678275))
