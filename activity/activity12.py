x=0
even=0
odd=0
num= eval(input("enter number lol: "))
num+= 1
for x in range(1,num):
    
    
    if x % 2 == 0:
        even += x
        
    else:
        odd += x
    x+=1
print(f"sum of even is {even}")

print(f"sum of odd is {odd}")