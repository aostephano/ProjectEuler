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

print(finalList)

sumValue = 0
for line in finalList:
    print(max(line))
    sumValue += max(line)

print(sumValue)

# anyString = ""
#
# for element in data:
#     anyString += element+" "
#
# tempList = anyString.split(" ")
# tempList.pop() #remove last value
# myFinalList = []
# for element in tempList:
#     myFinalList.append(int(element))
#
# print(myFinalList)
#
# print(sum(myFinalList))