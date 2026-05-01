noOfLines = int(input())

for line in range(noOfLines):
    strOfInts = input()
    array = strOfInts.split(" ")
    intArr = [int(x) for x in array]

    biggestInt = 0
    sum = 0
    for number in intArr:
        sum += number
        if biggestInt < number:
            biggestInt = number

    sum -= biggestInt
    if sum == biggestInt:
        print("Output: YES")
    else:
        print("Output: NO")