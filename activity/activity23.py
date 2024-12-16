def act():
    print("INFO: a factorial function is inside activity23. please open activity24 to launch this function.\n")
    def factorial(num):
        fact=1
        for x in range(1,num+1):
            fact *= x
        return fact

