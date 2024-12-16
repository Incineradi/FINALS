def cc():
    print("INFO: code_challenge12 prints an arrow.\n")
    for e in range(0, 5):
        for a in range (5, e, -1):
            print(" ", end=" " )
        for b in range (0, e*2):
            print("*", end=" " )
        print()
    for f in range(5, 0, -1):
        for c in range (0, 4):
            print(" ", end=" " )
        for d in range (0, 2):
            print("*", end=" " )
        print()

    print("not sure how to make this one take inputs and produce accurate arrows")
        