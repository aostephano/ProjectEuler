#Code from https://pythonandr.com/2015/09/01/highly-divisible-triangular-number-project-euler-problem-12/
from func import *
# First Step
# First number 'check' to have 500 divisors
check = 2 ** 4 * 3 ** 4 * 5 ** 4 * 7 * 11

# Second Step
# Starting from 'check', iterate sequentially checking for the next 'triangle' number
while not isTriangleNumber(check):
    check += 1

# Third and Fourth Steps
# Calculate the last term of the series ('seriesLastTerm') that adds up to the newly calculated triangle number 'check'
seriesLastTerm = lastTerm(check)

# Iterate over triangle numbers checking for divisors > 500
while divisors(check) <= 500:
    # add the next term to check to get the next triangle number
    check += (seriesLastTerm + 1)
    seriesLastTerm += 1
print(check)

