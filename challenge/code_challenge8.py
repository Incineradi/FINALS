 

def cc():
    print("INFO: code_challenge8 will ask for 10 numbers and will sum up all your inputs.\n")
    print("enter 10 random numbers")
    num=0
    for x in range(1, 11):
        get = eval(input(f"enter random number ({x}): "))
        num += get
    print(f"the total sum of all numbers is {num}!")