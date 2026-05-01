code = list(input())
answer = ""

while len(code) > 0:
    if len(code) == 1:
        answer += "0"
        break;
    
    currentChar = code[0]
    nextChar = code[1]

    if currentChar == ".":
        code.remove(currentChar)
        answer += "0"
        continue;
    else:
        if nextChar == ".":
            answer += "1"
        else:
            answer += "2"
        code.remove(currentChar)
        code.remove(nextChar)
            
print(answer)