def cc():
    print("fahrenheit to celsius converter")

    f = eval(input("enter fahrenheit (number only): "))
    c= (f-32)*5/9

    print(f"{f} fahrenheit converted to celsius is {round(c,2)}")
