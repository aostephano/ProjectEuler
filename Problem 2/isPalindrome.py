def isPalindrome(number):
  strNumber = str(number)
  isPalindrome = False
  halfExtension = len(strNumber)/2
  haveRemainder = False

  #Verify if the Len of the String is Even
  if len(strNumber)%2:
    haveRemainder = True

  if haveRemainder:
    return isPalindrome
  else:
    # Iterate over the first Half of the number and Add all to a String var
    firstHalfExtensionInt = int(halfExtension)
    firstNumberHalf = ""
    for index in range(0, firstHalfExtensionInt):
      firstNumberHalf += str(strNumber[index])
      
    # Iterate over the second Half of the number and Add all to a String var
    strNumberExtension = int(len(strNumber))
    secondNumberHalf = ""
    for index in range(firstHalfExtensionInt, strNumberExtension):
      secondNumberHalf += str(strNumber[index])

    reversedSecondHalf = secondNumberHalf[::-1]

    #Compares each String to see if its Palindrome
    for index in range(0, firstHalfExtensionInt):
      if firstNumberHalf[index] != reversedSecondHalf[index]:
        return isPalindrome

    isPalindrome = True
    return isPalindrome



isPalindrome(0)

