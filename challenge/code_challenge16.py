def cc():
    import os
    dep=0
    program=True
    ##########################################################################################

    name= input("enter name: ")
    def total(dep):
        d1000 = dep // 1000
        fivehundred = dep - (d1000*1000)
        d500 = fivehundred//500
        twohundred = fivehundred - (d500*500)
        d200 = twohundred//200
        hundred = twohundred - (d200*200)
        d100 = hundred//100
        fifty = hundred - (d100*100)
        d50 = fifty//50
        twenty = fifty - (d50*50)
        d20 = twenty//20
        ten = twenty - (d20*20)
        d10 = ten//10
        five = ten - (d10*10)
        d5 = five//5
        one = five - (d5*5)
        d1 = one//1
        print(

        f"\nhere is a breakdown of your balance: ",
        f"\n1000 - {d1000}",
        f"\n500 - {d500}",
        f"\n200 - {d200}",
        f"\n100 - {d100}",
        f"\n50 - {d50}",
        f"\n20 - {d20}",
        f"\n10 - {d10}",
        f"\n5 - {d5}",
        f"\n1 - {d1}",
        )
    dep += eval(input("initial deposit required (minimum of 10000): "))
    if dep <10000:
        os.system('cls')
        print("sorry, you are not eligible for an account.")
        quit()
    os.system('cls')
    print(
        f"\nwelcome {name}, what would you like to do today? ",
        )
    total(dep)
    print(f"\ncurrent balance: {dep}")


    while program:
        
        action = input("balance(1)/withdraw(2)/deposit(3)/quit(4): ")
        #####
        if action.lower()=="balance" or action=="1":
            os.system('cls')
            print(f"current balance: {dep}")
            total(dep)
        ######
        elif action.lower()=="withdraw" or action=="2":
            os.system('cls')
            
            if dep < 1:
                os.system('cls')
                print("no money to withdraw.")
                total(dep)
                print(f"\ncurrent balance: {dep}")
        ######
            else:
                withdraw = eval(input("enter the amount to withdraw: "))
                if dep - withdraw <0:
                    print(f"money withdrawn exceeded ({withdraw}).")
                    print(f"current balance: {dep}")
                else:
                    dep -= withdraw
                    total(dep)
                    print(f"\ncurrent balance: {dep}")
        ######
        elif action.lower()=="deposit" or action=="3":
            os.system('cls')
            dep += eval(input("enter your deposit: "))
            total(dep)
            print(f"\ncurrent balance: {dep}")
        ######
        elif action.lower()=="quit" or action=="4":
            os.system('cls')
            print("bye")
            break
        #####
        else:
            os.system('cls')
            print("input unrecognized.")
        
            