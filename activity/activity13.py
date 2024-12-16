def act():
    print("INFO: this program will calculate the factorial of your input.\n")
    num= input("enter number lol: ")
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
    fact=1
    for x in range(1,num+1):
        fact *= x
        
    print(f"factorial of {num} is {fact}")