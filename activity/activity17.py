def act():
    print("INFO: activity17 is a target 3 recap. it will ask for a number and will create a multiplication table up to your specified amount.\n")
    column = eval(input("enter number: ")) 
    column+=1
    for x in range(1, 11):
        for y in range(1, column):
            print(f"{x}x{y}={x*y}", end="\t")
        print()