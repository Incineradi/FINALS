def act():
    print("INFO: activity4 showcases the different operators of python and will calculate two inputs, similar to code_challenge4.\n")
    num1 = input("\n  type number lol: ")
    num2 = input("\n  type number lol: ")
            

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

    print()
    sum= num1 + num2
    diff= num1 - num2
    prod= num1 * num2
    quot= num1 / num2
    exp= num1 ** num2
    rem= num1 % num2
    floor= num1 // num2

    print(f"the sum of {num1} and {num2} is {sum}")
    print(f"the difference of {num1} and {num2} is {diff}")
    print(f"the product of {num1} and {num2} is {prod}")
    print(f"the quotient of {num1} and {num2} is {quot}")
    print(f"{num1} exponent by {num2} is {exp}")
    print(f"the remainder of {num1} and {num2} is {rem}")
    print(f"the floor division of {num1} and {num2} is {floor}")
