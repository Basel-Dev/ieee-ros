noOfLines = int(input())

for line in range(noOfLines):
    strOfInts = input()
    array = strOfInts.split(" ")

    biggestInt = 0
    sum = 0
    for number in array:
        intNum = int(number)
        sum += intNum
        if biggestInt < intNum:
            biggestInt = intNum

    sum -= biggestInt
    if sum == biggestInt:
        print("YES")
    else:
        print("NO")