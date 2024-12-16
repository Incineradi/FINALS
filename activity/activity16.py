
def act():
    print("INFO: activity16 is a cc9 recap.\n")
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