def act():
    print("INFO: this program will continuously ask for a name until you input 'stop'. the program will then count the amount of names you registered.\n")
    import os

    program=True
    count=0
    
    while program ==True:
        act=input("enter a name: ")
        count+=1
        if act.lower() =="stop":
            print(f"you typed {count} names.")
            print("program terminated")
            break

