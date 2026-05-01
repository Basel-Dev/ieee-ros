noOfLines = int(input())

for line in range(noOfLines):
    length = int(input())
    arr = input().split(" ")

    tallyDict = dict.fromkeys(set(arr), 0)

    for i in range(length):
        tallyDict[arr[i]] += 1
    
    spyElement = min(tallyDict, key=tallyDict.get)
    
    print(arr.index(spyElement)+1)