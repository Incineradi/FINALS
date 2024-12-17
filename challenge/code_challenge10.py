

def cc():
    print("INFO: code_challenge10 will produce a diamond of a size proportionate to the user's input.\n")
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
    for x in range(0, num):
        for ts in range (num, x, -1):
            print(" ", end=" " )

        for tt in range (0, x*2+1):
            print("*", end=" " )

        print()

    for y in range(num, 0, -1):
        for bs in range (num+2, y, -1):
            print(" ", end=" " )

        for bt in range (0, y*2-3):
            print("*", end=" " )

        print()
