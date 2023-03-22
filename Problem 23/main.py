def isAbundant(number):
    sumValue = 0
    for loop in range(1, int((number/2)+1)):
        if number%loop == 0:
            sumValue += loop

    if sumValue > number:
        return True
    else:
        return False


abundantList = []
# print(type(abundantList))

for number in range(1, 28124):
    if isAbundant(number):
        abundantList.append(number)
    else:
        pass

# for loop in range(0,10):
#     simpleList.append(loop)
#
# for first in simpleList:
#     for second in simpleList:
#         print(first)
#         print(second)

##Add sum abundant values into a set
abundantSumSet = set()
for first in abundantList:
    for second in abundantList:
        abundantSum = first + second
        if abundantSum < 28123:
            abundantSumSet.add(abundantSum)
        else:
            break

# Compares values from set with a list

nonAbundantValues = []
for number in range(0, 28123):
    if number not in abundantSumSet:
        nonAbundantValues.append(number)
    else:
        pass

print(sum(nonAbundantValues))
