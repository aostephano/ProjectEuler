from isPalindrome import isPalindrome

palindromeList = []
multiplier = 99
multiplicand = 100

multiplierCount = 0
multiplicandCount = 0

while(multiplier < 1000):
    multiplier += 1
    result = multiplier*multiplicand
    multiplierCount += 1

    if isPalindrome(result):
        print("Multiplier:", multiplier)
        print("Multiplicand:", multiplicand)
        print("Palindrome added:", result)
        palindromeList.append(result)

    while(multiplicand < 1000):
        multiplicand += 1
        result = multiplier*multiplicand
        multiplicandCount += 1
        if isPalindrome(result):
            print("Multiplier:", multiplier)
            print("Multiplicand:", multiplicand)
            print("Palindrome added:", result)
            palindromeList.append(result)
    
    multiplicand = 10

print("---")
print("Multiplier Counter:", multiplierCount)
print("Multiplicand Counter:", multiplicandCount)
print("Largest palindrome made from the product of two three digits numbers:", max(palindromeList))

"""
while(multiplier<100 and multiplicand<100):
  #print("Multiplier:", multiplier)
  #print("Multiplicand", multiplicand)

  multiplier += 1
  result = multiplier*multiplicand
  multiplierCount += 1
  if isPalindrome(result):
    print("Multiplier:", multiplier)
    print("Multiplicand:", multiplicand)
    print("Palindrome added:", result)
    palindromeList.append(result)

  multiplicand += 1
  result = multiplier*multiplicand
  multiplicandCount += 1
  if isPalindrome(result):
    print("Multiplier:", multiplier)
    print("Multiplicand:", multiplicand)
    print("Palindrome added:", result)
    palindromeList.append(result)
"""