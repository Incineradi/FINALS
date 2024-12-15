 

def cc():
    print("enter 10 random numbers")
    num=0
    for x in range(1, 11):
        get = eval(input(f"enter random number ({x}): "))
        num += get
    print(f"the total sum of all numbers is {num}!")