def cc():
    print("dont go past single digit numbers or it goes bonkers LOL")
    num = eval(input("\n  type number lol: "))
    num +=1
    if num > 10 :
        
        print("\ni literally just warned you man\n")
    else:

        for TOP in range(0, num):
            for A in range (num, TOP, -1):
                print(" ", end=" " )
            
            for B in range (TOP, 0, -1):
                print(B, end=" " )

            for C in range (2, TOP+1):
                print(C, end=" " )

            print()

        for BOTTOM in range(num, 0, -1):
            for A in range (num+2, BOTTOM, -1):
                print(" ", end=" " )

            for B in range (BOTTOM-2, 0, -1):
                print(B, end=" " )


            for C in range (2, BOTTOM-1):
                print(C, end=" " )

            print()
