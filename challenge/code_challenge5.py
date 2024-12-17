def cc():
    print("INFO: code_challenge5 is a fahrenheit to celsius converter like activity5.\n")
    print("fahrenheit to celsius converter")

    f = input("enter fahrenheit (number only): ")
    """FILTER CODE THAT IM VERY PROUD I MADE"""
    echo=f
    keep= "1234567890"
    for filterer in keep.lower(): 
        f = f.lower().replace(filterer,'')
    for converter in f:
        echo= echo.lower().replace(converter,'')
    if echo == "":
        echo="0"
    f=int(echo)
    """END OF THE FILTER CODE THAT IM VERY PROUD TO HAVE MADE"""
    c= (f-32)*5/9

    print(f"{f} fahrenheit converted to celsius is {round(c,2)}")
