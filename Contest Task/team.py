noOfLines = int(input())
numberToPrint = 0

for line in range(noOfLines):
    problem = input().split(" ")
    sum = 0

    for bit in problem:
        numBit = int(bit)
        sum += numBit

    if sum > 1:
        numberToPrint += 1
    else:
        continue;

print(numberToPrint)