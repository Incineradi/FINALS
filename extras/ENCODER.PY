def encoder():
    import os
    print("INFO: encoder encodes a specific number into a specific cipher formula. the creator utilized this program to make quick ciphers for their math activities.\n--------------------------------------------------------\n")
    
    program=True
    while program:
        dep= input("enter your number: ")
        if dep == "stop":
            os.system('cls')
            break
        """FILTER CODE THAT IM VERY PROUD I MADE"""
        echo=dep
        keep= "1234567890"
        for filterer in keep.lower(): 
            dep = dep.lower().replace(filterer,'')
        for converter in dep:
            echo= echo.lower().replace(converter,'')
        if echo == "":
            echo="0"
        dep=int(echo)
        """END OF THE FILTER CODE THAT IM VERY PROUD TO HAVE MADE"""

        fart= ((7*dep)+4) % 26
        print(fart)
        
## 8 3 14 13 14 19 3 4 18 4 17 21 4 19 7 8 18

## 1 4 6 4 13 19 11 4 22 8 19 7 12 24 7 4 0 17 19

