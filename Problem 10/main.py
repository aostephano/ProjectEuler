from sympy import *
from math import sqrt, floor


def isPrimeLowPerformanceV1(number):
    # Return True for Prime Number and False Otherwise
    # V1) Test all divisors from 2 until Number(non inclusive)
    if number > 1:
        for loop in range(2, number):
            if number % loop == 0:
                # print("Inst prime")
                return False
        # print("Is a prime number")
        return True

    else:
        # Number above one aren't prime numbers
        # print("Inst prime")
        return False

def isPrimeLowPerformanceV2(number):
    # Return True for Prime Number and False Otherwise
    # V2) Test all divisors from 2 through sqrt(N)
    if number > 1:
        maxDivisor = floor(sqrt(number))
        for loop in range(2, maxDivisor+1):
            if number % loop == 0:
                # print("Inst prime")
                return False
        # print("Is a prime number")
        return True

    else:
        # Number above one aren't prime numbers
        # print("Inst prime")
        return False

def genPrimeListByGivenNumber(number):
    primeList = []
    for loop in range(0, number):
        if isPrimeLowPerformanceV2(loop):
            primeList.append(loop)

    print(sum(primeList))


genPrimeListByGivenNumber(2000000)
