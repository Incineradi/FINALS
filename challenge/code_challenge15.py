def cc():
    print("INFO: code_challenge15 is a program that continuously asks the user for more triangles of uniform proportion. ",
          "if user states 'no', the program will be terminated.\n--------------------------------------------------------\n")
    import os
    program=True
    num=0
    while program:
        q= input("do you want another triangle? type 'no' to exit. : ")
        """FILTER CODE THAT IM VERY PROUD I MADE"""
        echo=q
        keep= "1234567890"
        for filterer in keep.lower(): 
            q = q.lower().replace(filterer,'')
        for converter in q:
            echo= echo.lower().replace(converter,'')
            if echo == "":
                echo="0"
        q=int(echo)
        """END OF THE FILTER CODE THAT IM VERY PROUD TO HAVE MADE"""
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