noOfLines = int(input())

for line in range(noOfLines):
    length = int(input())
    cubesAndName = input().split(" ")

    cubes = list(cubesAndName[0])
    name = list(cubesAndName[1])

    cubeDict = dict.fromkeys(set(cubes), 0)
    nameDict = dict.fromkeys(set(name), 0)

    for i in range(length):
        cubeDict[cubes[i]] += 1
        nameDict[name[i]] += 1

    if cubeDict == nameDict:
        print("Output: YES")
    else:
        print("Output: NO")