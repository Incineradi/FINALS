def cc():
    print("INFO: code_challenge14 utilizes the while loop by continuously asking for a number until the user inputs '0' OR an invalid input such as a char. if user inputs '0', the program will sum up all the numbers you entered.\n")
    print("enter '0' to quit and add all numbers.")
    num=0
    program=True
    while program:
        q=eval(input("enter a number: "))
        num += q
        if q==0:
            print(f"{num} is the total sum of all the numbers you entered.")
            break