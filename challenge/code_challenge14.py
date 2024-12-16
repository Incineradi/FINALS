def cc():
    print("INFO: code_challenge14 utilizes the while loop by continuously asking for a number until the user inputs '0' OR an invalid input such as a char. if user inputs '0', the program will sum up all the numbers you entered.\n")
    print("enter '0' to quit and add all numbers.")
    num=0
    program=True
    while program:
        q=input("enter a number: ")
        """FILTER CODE THAT IM VERY PROUD I MADE"""
        echo=q
        keep= "1234567890"
        for filterer in keep.lower(): 
            q = q.lower().replace(filterer,'')
        for converter in q:
            echo= echo.lower().replace(converter,'')
            if echo == "":
                echo="0"
        q=int(echo)
        """END OF THE FILTER CODE THAT IM VERY PROUD TO HAVE MADE"""
        num += q
        if q==0:
            print(f"{num} is the total sum of all the numbers you entered.")
            break