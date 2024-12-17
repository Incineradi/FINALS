def act():
    print("INFO: activity15 creates a triangle using loop.\n--------------------------------------------------------\n")
    for x in range(0, 11):
        print(x,end=" ")
        for y in range(0, x):
            print("*",end=" ")
        print()