def act():
    print("INFO: this program will ask for a number and will sum up odd and even numbers below or equal to the specified number .\n")
    x=0
    even=0
    odd=0
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
    num+= 1
    for x in range(1,num):
        
        
        if x % 2 == 0:
            even += x
            
        else:
            odd += x
        x+=1
    print(f"sum of even is {even}")

    print(f"sum of odd is {odd}")

