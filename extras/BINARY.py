def binary():
    print("INFO: binary converter.\n")
    
    num = input("type number: ")

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

    e=True
    while e:
        print(round(num,1), " = ", num % 2)

        num //= 2
        if num==0:
            break
