def act():
    print("INFO: activity17 is a target 3 recap. it will ask for a number and will create a multiplication table up to your specified amount.\n")
    num = input("enter number: ")
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
    for x in range(1, 11):
        for y in range(1, num):
            print(f"{x}x{y}={x*y}", end="\t")
        print()