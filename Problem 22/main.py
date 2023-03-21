file = open("p022_names.txt", "r")
anyList = []

for line in file:
    anyList.append(line.replace('"', "").split(","))

finalList = anyList[0]
sortedList = sorted(finalList)

alphabet_dict = {
    "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7,
    "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13,
    "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19,
    "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25,
    "Z": 26
}

def sumLetters(name):
    sumValue = 0
    for letter in name:
        sumValue += int(alphabet_dict[letter])

    return sumValue

totalScore = 0
for index, name in enumerate(sortedList, start= 1):

    prodValue = sumLetters(name)*int(index)
    totalScore += prodValue

print(totalScore)