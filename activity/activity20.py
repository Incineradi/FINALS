def act():
    print("INFO: this program will continuously ask whether you wish for another triangle or not.\n")
    import os

    the=True
    c=1
    act=input("want triangles? ")
    while the ==True:
        if act.lower() =="no":
            print("program terminated")
            break
        elif act.lower()=="yes":
            os.system("cls")
            c+=1
            for x in range(1, 6):
                for y in range(1, c):
                    for a in range(1, x+1):
                        print("*",end=" ")
                    for b in range(5, x, -1):
                        print(" ",end=" ")
                    print(end=" ")
                print()
        act=input("want MORE triangles? type 'no' to exit. ")
