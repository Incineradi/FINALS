

def cc():
    print("INFO: code_challenge9 will ask for a number and will convert it into a mirrored upside down triangle with the size equivalent to your input.\n")
    num = input("type number lol: ")
    """FILTER CODE THAT IM VERY PROUD I MADE"""
    echo=num
    keep= "1234567890"
    for filterer in keep.lower(): 
        num = num.lower().replace(filterer,'')
    for converter in num:
        echo= echo.lower().replace(converter,'')
    if echo == "":
        echo="0"
    num=int(echo)
    """END OF THE FILTER CODE THAT IM VERY PROUD TO HAVE MADE"""
    num += 1
    for x in range(0, num):
        for y in range (0, x):
            print(" ", end=" " )
    
        num -= 1
        for b in range (num, 0, -1):
            print("*", end=" " )

        print()