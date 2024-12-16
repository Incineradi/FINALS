def act():
    print("INFO: this program will calculate the factorial of your input.\n")
    num= eval(input("enter number lol: "))
    fact=1
    for x in range(1,num+1):
        fact *= x
        
    print(f"factorial of {num} is {fact}")