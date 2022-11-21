file = open("file.txt", "r")
anyList = []
for line in file:
    anyList.append(line)

# for any element in list, remove the last vector using "-1" negative indexing
data = [element[:-1] for element in anyList]

matrix = []
for line in data:
    matrix.append(line.split(" "))


def printMatrix(matrix):
    # # Go to all elements by position i,j
    for i, line in enumerate(matrix):
        for j, element in enumerate(line):
            print(element, end=" ")
        print("")


def upProd(i, j, matrix):
    # Function that receive line(i), column(j) and the matrix(matrix)
    # and calculate the 4 next elements above (Up)
    prodValue = 1
    for loop in range(0, 4):
        # Cant loop on negative list i
        if i - loop < 0:
            break
        # If reach index out bounds, stop calculate
        try:
            element = int(matrix[i - loop][j])
            # print("i:", i-loop,"j:", j)
        except IndexError:
            break
        prodValue *= element

    return prodValue


def downProd(i, j, matrix):
    # Function that receive line(i), column(j) and the matrix(matrix)
    # and calculate the 4 next elements above (Up)
    prodValue = 1
    for loop in range(0, 4):
        # If reach index out bounds, stop calculate
        try:
            element = int(matrix[i + loop][j])
            # print("i:", i + loop, "j:", j)
        except IndexError:
            break
        prodValue *= element

    return prodValue


def leftProd(i, j, matrix):
    # Function that receive line(i), column(j) and the matrix(matrix)
    # and calculate the 4 next elements above (Up)
    prodValue = 1
    for loop in range(0, 4):
        # Cant loop on negative list j
        if j - loop < 0:
            break
        # If reach index out bounds, stop calculate
        try:
            element = int(matrix[i][j - loop])
        except IndexError:
            break
        prodValue *= element

    return prodValue


def rightProd(i, j, matrix):
    # Function that receive line(i), column(j) and the matrix(matrix)
    # and calculate the 4 next elements above (Up)
    prodValue = 1
    for loop in range(0, 4):
        # If reach index out bounds, stop calculate
        try:
            element = int(matrix[i][j + loop])
        except IndexError:
            break
        prodValue *= element

    return prodValue


def diagoProd(i, j, matrix):
    # Function that receive line(i), column(j) and the matrix(matrix)
    # and calculate the 4 next elements above (Up)
    diagoValues = []
    # DownRight
    prodValue = 1
    for loop in range(0, 4):
        # If reach index out bounds, stop calculate
        try:
            element = int(matrix[i + loop][j + loop])
        except IndexError:
            break
        prodValue *= element
    diagoValues.append(prodValue)
    # DownLeft
    prodValue = 1
    for loop in range(0, 4):
        # Cant loop on negative list i
        if i - loop < 0:
            break
        # If reach index out bounds, stop calculate
        try:
            element = int(matrix[i - loop][j + loop])
        except IndexError:
            break
        prodValue *= element
    diagoValues.append(prodValue)
    # UpRight
    prodValue = 1
    for loop in range(0, 4):
        # Cant loop on negative list j
        if j - loop < 0:
            break
        # If reach index out bounds, stop calculate
        try:
            element = int(matrix[i + loop][j - loop])
        except IndexError:
            break
        prodValue *= element
    diagoValues.append(prodValue)
    # UpLeft
    prodValue = 1
    for loop in range(0, 4):
        # Cant loop on negative list i
        if i - loop < 0:
            break
        # Cant loop on negative list j
        if j - loop < 0:
            break
        # If reach index out bounds, stop calculate
        try:
            element = int(matrix[i - loop][j - loop])
        except IndexError:
            break
        prodValue *= element
    diagoValues.append(prodValue)

    return max(diagoValues)


greatestProduct = 0
for i, line in enumerate(matrix):
    for j, element in enumerate(line):
        elementMaxValue = max(upProd(i, j, matrix), downProd(i, j, matrix), leftProd(i, j, matrix),
                              rightProd(i, j, matrix), diagoProd(i, j ,matrix))
        if greatestProduct < elementMaxValue:
            greatestProduct = elementMaxValue

print(greatestProduct)

# print("Element(i:6, j:6):", matrix[5][5])
# downProd(5, 5, matrix)
