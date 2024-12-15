

def cc():
    num = eval(input("type number lol: "))
    num += 1
    for x in range(0, num):
        for y in range (0, x):
            print(" ", end=" " )
    
        num -= 1
        for b in range (num, 0, -1):
            print("*", end=" " )

        print()