def act():
    def factorial(num):
        fact=1
        for x in range(1,num+1):
            fact *= x
        return fact

