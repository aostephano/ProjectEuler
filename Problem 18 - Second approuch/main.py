#A second approuch after reading this example: https://www.r-bloggers.com/2017/04/euler-problem-18-67-maximum-path-sums/
# "A more efficient method is to define the maximum path layer by layer, starting at the bottom." 🤡

file = open("file.txt", "r")
anyList = []

for line in file:
    anyList.append(line)

# for any element in list, remove the last vector using "-1" negative indexing
data = [element.rstrip('\n') for element in anyList]

myNewList = []

for node in data:
    myNewList.append(node.split(" "))


finalList = []
tempLine = []
for line in myNewList:
    for node in line:
        tempLine.append(int(node))

    finalList.append(tempLine)
    tempLine = []

auxList = []
lastLine = []

# #[::-1] == Reverse Line Order, from botton to top
# for i, line in enumerate(finalList[::-1]):
#     for j, node in enumerate(line):
#         print(node)
#         try:
#             pass
#             parentNode = finalList[i - 1][j]
#             print("PNode:", parentNode)
#             childLeftNode = finalList[i][j]
#             childRightNode = finalList[i][j + 1]
#             parentNode += max(childLeftNode, childRightNode)
#             finalList[i - 1][j] = parentNode
#             print("LChild:", childLeftNode, "RChild:", childRightNode)
#             print("sumValue:", parentNode)
#         except:
#             print("Index out of bounds")
#             pass

for i in range(len(finalList)-1, 0, -1):
    for j in range(len(finalList[i])-1):
        parentNode = finalList[i - 1][j]
        print("PNode:", parentNode)
        childLeftNode = finalList[i][j]
        childRightNode = finalList[i][j + 1]
        parentNode += max(childLeftNode, childRightNode)
        finalList[i - 1][j] = parentNode
        print("LChild:", childLeftNode, "RChild:", childRightNode)
        print("sumValue:", parentNode)

for line in finalList:
    print(line)