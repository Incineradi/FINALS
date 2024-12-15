def cc():
    print("enter '0' to quit and add all numbers.")
    num=0
    program=True
    while program:
        q=eval(input("enter a number: "))
        num += q
        if q==0:
            print(f"{num} is the total sum of all the numbers you entered.")
            break