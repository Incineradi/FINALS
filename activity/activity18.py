def act():
    print("INFO: this program will continuously ask for a name until you input 'stop'.\n")
    import os

    the=True

    
    while the ==True:
        act=input("enter a name: ")
        if act.lower() =="stop":
            print("program terminated")
            break

