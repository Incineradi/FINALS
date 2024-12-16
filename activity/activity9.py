def act():
    print("INFO: this program identifies which age bracket you belong in.\n")
    age = eval(input("\ntype age lol: "))

    if age <1:
        print("invalid")

    elif age <8:
        print("toddler")
    elif age <14:
        print("pre-teen")
    elif age <19:
        print("teen")
    elif age <32:
        print("early adulthood")
    elif age <46:
        print("mid adulthood")
    elif age <59:
        print("post adulthood")
        
    elif age >100:
        print("you're probably dead lol")
    elif age >60:
        print("senior")