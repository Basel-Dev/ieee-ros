noOfLines = int(input())

def returnWord(str):
    if (len(str) <= 10):
        return str
    else: 
        arrStr = list(str)
        firstLetter = arrStr[0]
        lastLetter = arrStr[len(arrStr)-1]
        number = len(arrStr)-2

    return f"{firstLetter}{number}{lastLetter}"

for line in range(noOfLines):
    word = input()
    print(returnWord(word))

