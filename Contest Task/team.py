noOfLines = int(input())
numberToPrint = 0

for line in range(noOfLines):
    problem = [int(x) for x in input().split(" ")]
    sum = 0

    for bit in problem:
        sum += bit

    if sum > 1:
        numberToPrint += 1
    else:
        continue;

print(f"Output: {numberToPrint}")