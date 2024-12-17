def f( ):
    
    print("INFO: this is the final outcome of the filter program created by me, sean alonzo. :33333.\n")
    example=input("input a mix of numbers and strings. string only inputs will result into 0: ")
    echo=example
    keep= "1234567890."
    for filterer in keep.lower(): 
        example = example.lower().replace(filterer,'')
    for converter in example:
        echo= echo.lower().replace(converter,'')
        if echo == "":
            echo="0"
    example=float(echo)
    print(example)

#example="asf123"
#"""FILTER CODE THAT IM VERY PROUD I MADE"""
#echo=example
#keep= "1234567890"
#for filterer in keep.lower(): 
#    example = example.lower().replace(filterer,'')
#for converter in example:
#    echo= echo.lower().replace(converter,'')
#    if echo == "":
#        echo="0"
#example=int(echo)
#"""END OF THE FILTER CODE THAT IM VERY PROUD TO HAVE MADE"""
#
#"""made by me, sean alonzo. thats how proud i am :3333333"""