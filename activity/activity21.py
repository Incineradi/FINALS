
import os
os.system("cls")
num = eval(input("type number: "))
e=True
while e:
    print(round(num,1), " = ", num % 2)

    num //= 2
    if num==0:
        break