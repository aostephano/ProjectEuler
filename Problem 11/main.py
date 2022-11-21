file = open("anotherFile.txt", "r")
anyList = []
for line in file:
    anyList.append(line)

# for any element in list, remove the last vector using "-1" negative indexing
data = [element[:-1] for element in anyList]

matrix = []
for line in data:
    matrix.append(line.split(" "))

print(matrix)


def upSum(i, j, matrix):
    prodValue = 1
    for loop in range(0, 4):
        # Cant use negative values
        # Go Up
        line = i - loop
        column = j
        if line < 0:
            break
        if column < 0:
            break
        try:
            element = int(matrix[line][column])
        except IndexError:
            break
        prodValue += element
    return prodValue


def downSum(i, j, matrix):
    prodValue = 1
    for loop in range(0, 4):
        # Cant use negative values
        # Go Down
        line = i + loop
        column = j
        if line < 0:
            break
        if column < 0:
            break
        try:
            element = int(matrix[line][column])
        except IndexError:
            break
        prodValue += element
    return prodValue


def leftSum(i, j, matrix):
    prodValue = 1
    for loop in range(0, 4):
        # Cant use negative values
        # Go Left
        line = i
        column = j - 1
        if line < 0:
            break
        if column < 0:
            break
        try:
            element = int(matrix[line][column])
        except IndexError:
            break
        prodValue += element
    return prodValue


def rightSum(i, j, matrix):
    prodValue = 1
    for loop in range(0, 4):
        # Cant use negative values
        # Go Left
        line = i
        column = j + 1
        if line < 0:
            break
        if column < 0:
            break
        try:
            element = int(matrix[line][column])
        except IndexError:
            break
        prodValue += element
    return prodValue


maxProdValue = 0
# Go to all elements by position i,j
for i, line in enumerate(matrix):
    for j, element in enumerate(line):
        # print("i:", i, "j:", j)
        elementMaxProd = max(upSum(i, j, matrix), downSum(i, j, matrix), leftSum(i, j, matrix), rightSum(i, j, matrix))
        if maxProdValue < elementMaxProd:
            maxProdValue = elementMaxProd

print(maxProdValue)
