noOfLines = int(input())
currentCapacity = 0
maximumCapacity = 0

for line in range(noOfLines):
    arr = input().split(" ")
    exitingNum = int(arr[0])
    enteringNum = int(arr[1])

    if currentCapacity == 0:
        currentCapacity = enteringNum
    else:
        currentCapacity = currentCapacity + enteringNum - exitingNum

    if maximumCapacity < currentCapacity:
        maximumCapacity = currentCapacity

print(f"Output: {maximumCapacity}")
