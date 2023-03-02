base = 2
exponent = 1000

result = pow(base, exponent)
myList = list(str(result))

newList = []
for element in myList:
    newList.append(int(element))

mySum = sum(newList)

print(mySum)