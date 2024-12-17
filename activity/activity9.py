
def act():
    print("INFO: this program identifies which age bracket you belong in.\n")
    age = input("\ntype age lol: ")

    echo=age
    keep= "1234567890"
    for filterer in keep.lower(): 
        age = age.lower().replace(filterer,'')
    for converter in age:
        echo= echo.lower().replace(converter,'')
    if echo == "":
        echo="0"
    age=int(echo)

    if age <1:
        print(f"{age} is not a valid age.")

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
