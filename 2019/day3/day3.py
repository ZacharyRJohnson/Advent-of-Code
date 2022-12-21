def readInput(file):
    instructions = []
    with open(file) as f:
        cables = f.read().split()
        for cable in cables:
            instructions.append(cable.split(","))
    return instructions

def processInput(instructions):
    processedInput = []
    for cable in instructions:
        processedCable = []
        start = [0, 0]
        processedCable.append(start)
        for instruction in cable:
            end = []
            if(instruction[0] == 'R'):
                end = [start[0] + int(instruction[1:]), start[1]]
            elif(instruction[0] == 'L'):
                end = [start[0] - int(instruction[1:]), start[1]]
            elif(instruction[0] == 'U'):
                end = [start[0], start[1] + int(instruction[1:])]
            elif(instruction[0] == 'D'):
                end = [start[0], start[1] - int(instruction[1:])]
            processedCable.append(end)
            start = end
        processedInput.append(processedCable)
    return processedInput

def checkIntersect(cables, inst):
    cable1 = cables[0]
    cable2 = cables[1]
    inst1 = inst[0]
    inst2 = inst[1]
    intersections = []
    steps1 = 0
    for i in range(0, len(cable1) - 1):
        start1 = cable1[i]
        end1 = cable1[i + 1]
        dy1 = end1[1] - start1[1]
        dx1 = start1[0] - end1[0]
        c1 = dy1*start1[0] + dx1*start1[1]
        dy2 = 0
        dx2 = 0
        steps2 = 0

        for j in range(0, len(cable2) - 1):
            start2 = cable2[j]
            end2 = cable2[j + 1]
            dy2 = abs(end2[1] - start2[1])
            dx2 = abs(start2[0] - end2[0])
            c2 = dy2*start2[0] + dx2*start2[1]

            determinant = dy1*dx2 - dy2*dx1
            if(determinant != 0):
                x = (dx2*c1 - dx1*c2)/determinant
                y = (dy1*c2 - dy2*c1)/determinant
                tmp1 = abs(x - start1[0]) + abs(y - start1[1])
                tmp2 = abs(x - start2[0]) + abs(y - start2[1])
                if(x >= min([end1[0], start1[0]]) and x <= max([end1[0], start1[0]]) and x >= min([end2[0], start2[0]]) and x <= max([end2[0], start2[0]])):
                    if(y >= min([end1[1], start1[1]]) and y <= max([end1[1], start1[1]]) and y >= min([end2[1], start2[1]]) and y <= max([end2[1], start2[1]])):
                        if(x != 0 and y != 0):
                            intersections.append([x, y, tmp1 + tmp2 + steps1 + steps2])

            steps2 += int(inst2[j][1:])
        steps1 += int(inst1[i][1:])

    return intersections

def minDistance(points):
    minimum = abs(points[0][0]) + abs(points[0][1])
    for point in points:
        dist = abs(point[0]) + abs(point[1])
        minimum = dist if (minimum > dist) else minimum
    return minimum 

def minSteps(points):
    minimum = abs(points[0][2])
    for point in points:
        step = point[2]
        minimum = step if (minimum > step ) else minimum
    return minimum 

inst = readInput("input1.txt")
cables = processInput(inst)
points = checkIntersect(cables, inst)
print(minDistance(points))
print(minSteps(points))