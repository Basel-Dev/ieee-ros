noOfLines = int(input())

for line in range(noOfLines):
    length = int(input())
    arr = input().split(" ")
    intArr = [int(x) for x in arr]

    maxInt = max(intArr)
    
    numOfOperations = 0

    while set(intArr) != set([maxInt]):
        for i in range(length):
            if intArr[i] < maxInt:
                intArr[i] += 1
        numOfOperations += 1

    print(f"Output: {numOfOperations}")