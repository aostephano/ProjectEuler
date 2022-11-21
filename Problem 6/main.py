def sumSquareOfGivenNumber(number):
    numberList = []

    for value in range(0, number+1):
        numberList.append(pow(value, 2))

    return sum(numberList)

def squareOfSumOfGivenNumber(number):
    squareSum = 0
    for value in range(0, number+1):
        squareSum += value
    return pow(squareSum, 2)

def differenceBetween(first, second):
    diff = second - first
    return diff

first = sumSquareOfGivenNumber(100)
second = squareOfSumOfGivenNumber(100)
print(differenceBetween(first, second))