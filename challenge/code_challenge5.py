def cc():
    print("INFO: code_challenge5 is a fahrenheit to celsius converter like activity5.\n")
    print("fahrenheit to celsius converter")

    f = eval(input("enter fahrenheit (number only): "))
    c= (f-32)*5/9

    print(f"{f} fahrenheit converted to celsius is {round(c,2)}")
