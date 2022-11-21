file = open("file.txt", "r")
anyList = []
for line in file:
    anyList.append(line)

# for any element in list, remove the last vector using "-1" negative indexing
data = [element[:-1] for element in anyList]

finalSum = 0
for element in data:
    finalSum += int(element)

print("Int Sum:", finalSum)

stringSum = str(finalSum)
# for idx, char in enumerate(stringSum):
#     print(idx)

firstTen = 0
myString = ""
for loop in range(0, 10):
    myString += stringSum[loop]

print((myString))