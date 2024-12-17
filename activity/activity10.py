def act():
    print("INFO: this program identifies what your classification is based on your school year. please input the correct number from numbers 1-4.\n--------------------------------------------------------\n")
    name = input("\ntype name lol: ")
    dll = input("\nare you a student of dll?: ")

    if dll.lower() =="yes":
        yr=input("\nwhat is your year level? (1-4): ")

        """FILTER CODE THAT IM VERY PROUD I MADE"""
        echo=yr
        keep= "1234567890"
        for filterer in keep.lower(): 
            yr = yr.lower().replace(filterer,'')
        for converter in yr:
            echo= echo.lower().replace(converter,'')
        if echo == "":
            echo="0"
        yr=int(echo)
        """END OF THE FILTER CODE THAT IM VERY PROUD TO HAVE MADE"""

        if yr == 1:
            print("Welcome to dll, freshman.")
        elif yr == 2:
            print("Welcome to dll, sophomore.")
        elif yr == 3:
            print("Welcome to dll, junior.")
        elif yr == 4:
            print("Welcome to dll, senior.")
        else:
            print("input a proper number next time.")
    else:
        print("ok")