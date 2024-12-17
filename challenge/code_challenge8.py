 

def cc():
    print("INFO: code_challenge8 will ask for 10 numbers and will sum up all your inputs.\n")
    print("enter 10 random numbers")
    num=0
    for x in range(1, 11):
        get = input(f"enter random number ({x}): ")
        """FILTER CODE THAT IM VERY PROUD I MADE"""
        echo=get
        keep= "1234567890"
        for filterer in keep.lower(): 
            get = get.lower().replace(filterer,'')
        for converter in get:
            echo= echo.lower().replace(converter,'')
        if echo == "":
            echo="0"
        get=int(echo)
        """END OF THE FILTER CODE THAT IM VERY PROUD TO HAVE MADE"""
        num += get
    print(f"the total sum of all numbers is {num}!")
