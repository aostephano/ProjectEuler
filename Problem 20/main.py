# Python code to demonstrate naive method
# to compute factorial

n = 100
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("The factorial of",n,":",fact)

sumValue = 0
for digit in str(fact):
    sumValue += int(digit)

print("SumValue:", sumValue)