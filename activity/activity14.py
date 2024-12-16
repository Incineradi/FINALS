def act():
    print("INFO: this program will ask for a specified snake length (anybody who says it isn't a snake will not witness the light of day).\n")
    num= input("enter length number lol: ")
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
    for x in range(0,num):
        print("=",end="")
    print("*>-")