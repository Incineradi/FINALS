def act():
    print("INFO: this program will continuously ask whether you wish for another triangle or not.\n")
    import os

    the=True

    act=input("enter a name: ")
    while the ==True:
        if act.lower() =="stop":
            print("program terminated")
            break

