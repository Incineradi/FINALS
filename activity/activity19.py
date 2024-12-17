def act():
    print("INFO: this program will ask for a specified amount of triangles to produce.\n")
    num=input("enter amount of triangles: ")

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

    num+=1
    for x in range(1, 6):
        for y in range(1, num):
            for a in range(1, x+1):
                print("*",end=" ")
            for b in range(5, x, -1):
                print(" ",end=" ")
            print(end=" ")
        print()
