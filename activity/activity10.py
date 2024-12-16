def act():
    print("INFO: this program identifies what your classification is based on your school year. please input the correct number from numbers 1-4.\n")
    name = input("\ntype name lol: ")
    dll = input("\nare you a student of dll?: ")

    if dll.lower() =="yes":
        yr=eval(input("\nwhat is your year level? (1-4): "))
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