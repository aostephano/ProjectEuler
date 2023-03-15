file = open("file.txt", "r")
anyList = []

for line in file:
    anyList.append(line)

# for any element in list, remove the last vector using "-1" negative indexing
data = [element.rstrip('\n') for element in anyList]

myNewList = []

for element in data:
    myNewList.append(element.split(" "))

finalList = []
tempLine = []
for line in myNewList:
    for element in line:
        tempLine.append(int(element))

    finalList.append(tempLine)
    tempLine = []

auxList = []
def greaterNumber(myNewList, lastPos):
    firstValue = 0
    greatAdj = 0
    line = lastPos[0]
    column = lastPos[1]
    leftNumber = 0
    rightNumber = 0

    #Is the first number of the List? [0][0]
    if line == 0 and column == 0:
        firstValue = int(myNewList[line][column])
        auxList.append(firstValue)

    print("-----")
    print("Actual:", myNewList[line][column])

    try:
        leftNumber = int(myNewList[line + 1][column])
        rightNumber = int(myNewList[line + 1][column + 1])
        print("Left:", leftNumber, "Right:", rightNumber)
    except:
        lastValue = 0
        lastColumn = column+1 #go to next column
        lastLine = line
        lastPos = (lastLine, lastColumn)
        return lastValue, lastPos

    greatAdj += int(leftNumber if leftNumber >= rightNumber else rightNumber)
    auxList.append(greatAdj)
    print("Greater Value:", greatAdj)

    lastColumn = column if greatAdj == leftNumber else column+1
    lastLine = line+1
    print("lastLine:", lastLine, "lastColumn:", lastColumn)

    lastPos = (lastLine, lastColumn)
    lastValue = (int(greatAdj)+int(firstValue))

    return lastValue, lastPos

lastPos = (0,0)
auxPos = (0,0)
lastValue = 0
sumValue = 0

for line in myNewList:
    for number in line:
        lastValue, auxPos = greaterNumber(myNewList, lastPos)
        lastPos = auxPos
        sumValue += lastValue
        break #force to go to the next line after reaching the adj greatest number

print(auxList)
print("SumValue:", sumValue)
