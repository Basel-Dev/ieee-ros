noOfLines = int(input())
numToPrint = 0

for line in range(noOfLines):
    intArr = input().split(" ")
    peopleWhoAlready = int(intArr[0])
    totalAvailable = int(intArr[1])

    if peopleWhoAlready + 2 <= totalAvailable:
        numToPrint += 1
    else:
        continue;

print(numToPrint)