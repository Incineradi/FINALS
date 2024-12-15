num=eval(input("enter num: "))
num+=1
for x in range(1, 6):
    for y in range(1, num):
        for a in range(1, x+1):
            print("*",end=" ")
        for b in range(5, x, -1):
            print(" ",end=" ")
        print(end=" ")
    print()
