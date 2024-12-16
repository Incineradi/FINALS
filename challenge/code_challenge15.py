def cc():
    print("INFO: code_challenge15 is a program that continuously asks the user for more triangles of uniform proportion. if user states 'no', the program will be terminated.\n")
    import os
    program=True
    num=0
    while program:
        q= input("do you want another triangle?: ")

        if q.lower()=="yes":
            os.system('cls')
            num+=1
            for x in range(1, 6):
                for a in range(1, num+1):
                    for b in range(1, x+1):
                        print("*", end=" ")
                    for c in range(6,x, -1):
                        print(" ", end=" ")
                print()
        elif q.lower()=="no":
            print("terminated")
            break
        else:
            os.system('cls')
            print("error")