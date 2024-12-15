import os
program=True
while program:
    dep= eval(input("enter your number: "))
    fart= ((7*dep)+4) % 26
    print(fart)
    if dep == -1:
        os.system('cls')
        break
## 8 3 14 13 14 19 3 4 18 4 17 21 4 19 7 8 18

## 1 4 6 4 13 19 11 4 22 8 19 7 12 24 7 4 0 17 19