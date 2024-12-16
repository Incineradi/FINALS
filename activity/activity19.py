def act():
    print("INFO: this program will ask for a specified amount of triangles to produce.\n")
    num=eval(input("enter amount of triangles: "))
    num+=1
    for x in range(1, 6):
        for y in range(1, num):
            for a in range(1, x+1):
                print("*",end=" ")
            for b in range(5, x, -1):
                print(" ",end=" ")
            print(end=" ")
        print()
