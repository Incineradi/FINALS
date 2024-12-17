def cc():
    print("INFO: code_challenge13 creates a diamond made of numbers. 2 digit numbers are not adviced because it ruins the diamond. i could use the tab command, but i kinda dont care and we werent instructed to use it. it will also make the diamond look bigger.\n")
    print("dont go past single digit numbers or it goes bonkers LOL")
    num = input("\n  type number lol: ")
    """FILTER CODE THAT IM VERY PROUD I MADE"""
    echo=num
    keep= "1234567890"
    for filterer in keep.lower(): 
        num = num.lower().replace(filterer,'')
    for converter in num:
        echo= echo.lower().replace(converter,'')
    if echo == "":
        echo="0"
    num=int(echo)
    """END OF THE FILTER CODE THAT IM VERY PROUD TO HAVE MADE"""
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
