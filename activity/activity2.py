
def act():
    print("INFO: this program will divide two inputs.\n--------------------------------------------------------\n")
    num1 = input("\n  type 1st number lol: ")
    num2 = input("\n  type 2nd number lol: ")

    """FILTER CODE THAT IM VERY PROUD I MADE"""
    echo=num1
    echo1=num2
    keep= "1234567890"
    for filterer in keep.lower(): 
        num1 = num1.lower().replace(filterer,'')
        num2 = num2.lower().replace(filterer,'')
    for converter in num1:
        echo= echo.lower().replace(converter,'')
    if echo == "":
        echo="0"
    for converter in num2:
        echo1= echo1.lower().replace(converter,'')
        if echo1 == "":
            echo1="0"
    num1=int(echo)
    num2=int(echo1)
    """END OF THE FILTER CODE THAT IM VERY PROUD TO HAVE MADE"""

    print(f"{num1} / {num2} = {num1/num2}")
