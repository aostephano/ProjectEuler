file = open("file.txt", "r")
anyList = []
for line in file:
    anyList.append(line)

# for any element in list, remove the last vector using "-1" negative indexing
data = [element[:-1] for element in anyList]

# add the element in a string
anyString = ""
for element in data:
    anyString += element

finalList = []
# Iterate in all vectors in the string
for vector in range(0, len(anyString)):
    finalList.append(anyString[vector])

listOfValues = []
lastElementPos = len(finalList)
initialIndex = 0
prodValue = 1

finalProductFound = False

while not finalProductFound:
    if initialIndex + 13 > lastElementPos - 1:
        for loop in range(0, 13):
            elementInList = int(finalList[initialIndex + loop])
            prodValue *= elementInList
        initialIndex += 1
        listOfValues.append(prodValue)
        finalProductFound = True
    else:
        for loop in range(0, 13):
            elementInList = int(finalList[initialIndex + loop])
            prodValue *= elementInList
        initialIndex += 1
        listOfValues.append(prodValue)
        prodValue = 1

print(max(listOfValues))

#Para cada elemento na lista, faz o produto dos trinta seguintes e compara com a var
