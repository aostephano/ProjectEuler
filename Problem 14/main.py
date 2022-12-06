# n -> n/2 (if n is Even)
# n -> 3n+1 (if n is Odd)

def isEven(number):
    if number%2 == 0:
        return True
    else:
        return False
    
def reduceCollatz(number):
    return number/2

def increaseCollatz(number):
    return 3*number+1

def createCollatzSeq(number):
    lastInt = int(number)
    collatzSeq = [lastInt]

    while lastInt > 1:
        if isEven(lastInt):
            lastInt = reduceCollatz(lastInt)
            collatzSeq.append(lastInt)
        else:
            lastInt = increaseCollatz(lastInt)
            collatzSeq.append(lastInt)

    return collatzSeq


startNumb = 0
endNumb = 1000000
auxLen = 0
auxNumb = 0

while startNumb < endNumb:
    nextLen = len(createCollatzSeq(startNumb))
    if nextLen > auxLen:
        auxNumb = startNumb
        auxLen = nextLen

    startNumb += 1

print("Number:",auxNumb,"Len:",auxLen)