def sumProperDivisors(number):
    sumValue = 0

    for loop in range(1, int((number/2)+1)):
        if number%loop == 0:
            sumValue += loop

    return sumValue

def isAmicable(number):
    sumValue = sumProperDivisors(number)
    theSameNumberInPair = True if number == sumValue else False
    if sumProperDivisors(sumValue) == number and not theSameNumberInPair:
        return True
    else:
        return False


# print(isAmicable(6))


amicableSum = 0
for number in range(1, 10000+1):
    if isAmicable(number):
        amicableSum += number
    else:
        pass

print(amicableSum)