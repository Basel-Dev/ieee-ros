noOfLines = int(input())

for line in range(noOfLines):
    rating = int(input())
    
    print("Output: ", end="")

    if rating >= 1900:
        print("Division 1")
    elif rating >= 1600 and rating <= 1899:
        print("Division 2")
    elif rating >= 1400 and rating <= 1599:
        print("Division 3")
    else:
        print("Division 4")

