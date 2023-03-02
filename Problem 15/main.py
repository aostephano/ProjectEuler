# Math solution got from https://math.stackexchange.com/questions/286437/arrangement-of-binary-bits
# Python solution got from https://www.youtube.com/watch?v=mESH4k2SNZE

import time
import math

# solutions = []

def pathCounter(gridSize):
    p =  math.factorial(gridSize*2) / (math.factorial(gridSize)**2)
    # path = []
    # counter = 0
    # # Find ONE solution to the problem, starting with down, then right
    # for i in range(0, gridSize):
    #     path.append(0)
    #     path.append(1)
    #
    # print(path)
    #
    # for i in itertools.permutations(path, gridSize*2):
    #     if i not in solutions:
    #         solutions.append(i)
    #         counter = counter+1
            
    return p
    
tic = time.clock_gettime(time.CLOCK_BOOTTIME)
n = pathCounter(20)
toc = time.clock_gettime(time.CLOCK_BOOTTIME)
elapsed = toc-tic
print("%s found in %s seconds" % (n, elapsed))
