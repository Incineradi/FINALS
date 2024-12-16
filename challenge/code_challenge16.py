def cc():
    print("INFO: code_challenge16 is a bank simulator that asks for an initial deposit of 10000 to be eligible for an account.\n")
    print("this program is sort of long but not so annoying. if you wish to quit, type 0. otherwise, type enter.")
    annoying=input("")
    if annoying == "0":
        print("so relatable")
    else:
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
        dep = input("initial deposit required (minimum of 10000): ")


        """FILTER CODE THAT IM VERY PROUD I MADE"""
        echo=dep
        keep= "1234567890"
        for filterer in keep.lower(): 
            dep = dep.lower().replace(filterer,'')
        for converter in dep:
            echo= echo.lower().replace(converter,'')
            if echo == "":
                echo="0"
        dep=int(echo)
        """END OF THE FILTER CODE THAT IM VERY PROUD TO HAVE MADE"""


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
                    withdraw = input("enter the amount to withdraw: ")

                    """FILTER CODE THAT IM VERY PROUD I MADE"""
                    echo=withdraw
                    keep= "1234567890"
                    for filterer in keep.lower(): 
                        withdraw = withdraw.lower().replace(filterer,'')
                    for converter in withdraw:
                        echo= echo.lower().replace(converter,'')
                        if echo == "":
                            echo="0"
                    withdraw=int(echo)
                    """END OF THE FILTER CODE THAT IM VERY PROUD TO HAVE MADE"""


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
                add = input("enter your deposit: ")

                """FILTER CODE THAT IM VERY PROUD I MADE"""
                echo=add
                keep= "1234567890"
                for filterer in keep.lower(): 
                    add = add.lower().replace(filterer,'')
                for converter in add:
                    echo= echo.lower().replace(converter,'')
                    if echo == "":
                        echo="0"
                dep+=int(echo)
                """END OF THE FILTER CODE THAT IM VERY PROUD TO HAVE MADE"""


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
            
