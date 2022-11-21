# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any 
# remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#Problem 4

def haveRemainder(number, start, end):
    haveRemainder = False
    for dividend in range(start, end+1):      

        if (number%dividend)>0:
            haveRemainder = True
            return haveRemainder

    return haveRemainder

def isEven(number):
    if number%2 == 0:
        return True
    else:
        return False

def isTenMultiple(number):
    strNumber = str(number)
    if strNumber[len(strNumber)-1] == '0':
        return True
    else:
        return False

number = 0
foundSmallestNumber = False

while foundSmallestNumber == False:
    number += 20
    if isTenMultiple(number):
        if haveRemainder(number, 1, 20) == False:
            print("Found the smallest:", number)
            foundSmallestNumber = True

