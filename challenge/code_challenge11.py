
def cc():
    num = eval(input("\n  type number lol: "))
    print()
    for x in range(0, num):
        for ts in range (num, x, -1):
            print(" ", end=" " )

        for tt in range (0, x*2+1):
            print("*", end=" " )

        print()

    for y in range(num, 0, -1):
        for bs in range (num+2, y, -1):
            print(" ", end=" " )

        for bt in range (0, y*2-3):
            print("*", end=" " )

        print()
    print("yes its essentially the same thing cus i kind of already solved it in  cc10")