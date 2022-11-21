# By listing the first six prime numbers: 2, 3, 5, 7, 31, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

# Prime numbers are numbers greater than 1. They only have two factors, 1 and the number itself. This means these numbers cannot be
# divided by any number other than 1 and the number itself without leaving a remainder.

def isPrimeLowPerformance(number):
    if number > 1:
        for loop in range(2, number):
            if number % loop == 0:
                #print("Inst prime")
                return False
       #print("Is a prime number")
        return True

    else:
        # Number above one aren't prime numbers
        #rint("Inst prime")
        return False


primeCounter = 1
anyNumber = 2

while primeCounter <= 10001:
    foundPrime = False
    while not foundPrime:
        if not isPrimeLowPerformance(anyNumber):
            anyNumber += 1
        else:
            print("Prime", primeCounter, "o:", anyNumber)
            anyNumber += 1
            foundPrime = True
    primeCounter += 1

print(anyNumber)
