import itertools

digitsList = [value for value in range(0,10)]
permutationList = list(itertools.permutations(digitsList))

for idx in range(0, 1000000):
    if idx == 1000000-1:
        print(permutationList[idx])

