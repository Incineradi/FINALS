import os
##import cc
from challenge.code_challenge1 import cc as cc1
from challenge.code_challenge2 import cc as cc2
from challenge.code_challenge3 import cc as cc3
from challenge.code_challenge4 import cc as cc4
from challenge.code_challenge5 import cc as cc5
from challenge.code_challenge6 import cc as cc6
from challenge.code_challenge7 import cc as cc7
from challenge.code_challenge8 import cc as cc8
from challenge.code_challenge9 import cc as cc9
from challenge.code_challenge10 import cc as cc10
from challenge.code_challenge11 import cc as cc11
from challenge.code_challenge12 import cc as cc12
from challenge.code_challenge13 import cc as cc13
from challenge.code_challenge14 import cc as cc14
from challenge.code_challenge15 import cc as cc15
from challenge.code_challenge16 import cc as cc16

##import act
from activity.activity1 import act as act1
from activity.activity2 import act as act2
from activity.activity3 import act as act3
from activity.activity4 import act as act4
from activity.activity5 import act as act5
from activity.activity6 import act as act6
from activity.activity7 import act as act7
from activity.activity8 import act as act8
from activity.activity9 import act as act9
from activity.activity10 import act as act10
from activity.activity11 import act as act11
from activity.activity12 import act as act12
from activity.activity13 import act as act13
from activity.activity14 import act as act14
from activity.activity15 import act as act15
from activity.activity16 import act as act16
from activity.activity17 import act as act17
from activity.activity18 import act as act18
from activity.activity19 import act as act19
from activity.activity20 import act as act20
from activity.activity21 import act as act21
from activity.activity22 import act as act22
from activity.activity23 import act as act23
from activity.activity24 import act as act24
from activity.activity25 import act as act25


##import extras
from extras.ENCODER import encoder
from extras.BINARY import binary
from extras.testing import filtertest
from extras.filterer import f




"""people tell me these blocks of import look ugly but honestly they're so pretty to look at"""
def menuinf():
    os.system('cls')
    print(
    "\n                                 WELCOME TO MY CODE ARCHIVE!\n",

    "\n this program compiles programs created during the first sem for easier access.\n",
    "\n this includes code challenges, activities, and even programs that i made for personal use.",
    "\n this compiler tries its best to preserve the original code of the programs, ",
    "\n but modifies it a little to prevent unexpected termination of the compiler. \n",

    "\n with all that in mind, this compiler will also try its best to guide you through all of them.",
    "\n enjoy!\n",

    )
    click=input("\npress enter to continue: \n")
    

menuinf()
os.system('cls')

print("Welcome! i opened the general help list for you to get you started. if you ever wish to open this submenu again, type 'help'.")




def end():
    print("simulation ended.")
##for calling
def ccn(c):
    print(f"successfully imported code_challenge{c.lower().replace('c','')}\n")

def actn(c):
    print(f"successfully imported activity{c.lower().replace('act','')}\n")

def exn(c):
    print(f"successfully imported extras{c.lower().replace('ex','')}\n")



def intnotice():
    print(
    "\nNOTICE:\n",

    "\nit seems that this program contains a variable that asks for an INTEGER(or float) as an input. keep in mind that:\n",
    "\n -the program will detect and ignore special characters when doing so.",
    "\n if the user inputs 'asd123f' in an integer exclusive input, the output will be '123'.\n",


    "\n -if an input asks for an integer, '12.0' will convert into '120' because '.' is a special character.",
    "\n keep in mind this filter does not apply if the program is asking for a float number.\n",

    "\n -if the input is left empty, the program will detect it and replace it with 0.",


    )
    click=input("\npress enter to continue: \n")
    os.system('cls')



def actinf():
    print(
    "\nLIST of ACTIVITIES\n",

    "\n\n*PRINT STATEMENTS*\n",
    "\nACTIVITY 1: Hello world!",
    "\nDescription: first activity.\n",

    "\n\n*OPERATORS*\n",
    "\nACTIVITY 2: Division calculator",
    "\nDescription: divides two inputs.\n",

    "\nACTIVITY 3: Biodata",
    "\nDescription: simulates a biodata. very long program, and often times very annoying during testing. its a recap of code challenge 3.\n",

    "\nACTIVITY 4: Python operators",
    "\nDescription: uses the different python operators to calculate two inputs. its a recap of code challenge 4.\n",

    "\nACTIVITY 5: Fahrenheit to celsius",
    "\nDescription: its a recap of code challenge 5.\n",

    "\nACTIVITY 6: Addition assignment operator",
    "\nDescription: utilizes +=, which adds onto and updates the variable itself.\n",

    "\n\n*IF ELSE STATEMENTS*\n",
    "\nACTIVITY 7: Gold ownership",
    "\nDescription: utilizes if-else statements.\n",

    "\nACTIVITY 8: Login simulator",
    "\nDescription: also utilizes if-else statements. example provided when the program is opened.\n",

    "\nACTIVITY 9: Age bracket",
    "\nDescription: determines whether you are under a specific age bracket and classifies you.\n",

    "\nACTIVITY 10: School year",
    "\nDescription: classifies you based on your school year level IF you're a student of dll.\n",

    "\n\n*LOOP STATEMENTS*\n",
    "\nACTIVITY 11: Introduction to loop",
    "\nDescription: loops a statement 10 times.\n",

    "\nACTIVITY 12: Sum of odd and even numbers within a count range",
    "\nDescription: asks the user for a number. the program will count for a specified amount and add numbers with a similar classification (odd or even)\n",

    "\nACTIVITY 13: Factorial calculator",
    "\nDescription: the program will calculate the factorial of user input.\n",

    "\nACTIVITY 14: End in print",
    "\nDescription: simple loop program that converts input into the length size of a snake by modifying the print's end statement into ''.\n",

    "\nACTIVITY 15: Triangle",
    "\nDescription: creates a triangle using loop.\n",

    "\nACTIVITY 16: Mirrored upside down triangle",
    "\nDescription: creates a mirrored upside down triangle with a size proportionate to user input. this is a code challenge 9 recap.\n",

    "\nACTIVITY 17: Multiplication table",
    "\nDescription: creates a multiplication table of a size proportionate to user input.\n",

    "\nACTIVITY 18: Triangles",
    "\nDescription: asks the user for a specified amount of triangles to produce in a row.\n",

    "\nACTIVITY 19: under maintenance",
    "\nDescription: \n",

    "\nACTIVITY 20: While loop triangles",
    "\nDescription: continuously asks the user if they want to add a triangle in a row. this is a recap of code challenge 15.\n",

    "\nACTIVITY 21: under maintenance",
    "\nDescription: \n",

    "\n\n*FUNCTIONS*\n",
    "\nACTIVITY 22: Introduction to functions",
    "\nDescription: creates a function and calls it 4 times.\n",
    
    "\nACTIVITY 23: Outside function",
    "\nDescription: this program houses a function that isnt called. it is meant to be empty and executed by activity 24.\n",
    
    "\n\n*IMPORTS*\n",
    "\nACTIVITY 24: Introduction to imports",
    "\nDescription: this program imports a function from activity23 and calls it.\n",

    "\n\n*LISTS*\n",
    "\nACTIVITY 25: Introduction to lists",
    "\nDescription: this program utilizes list basics such as append, insert, and remove.\n",

    )
def ccinf():
    print(
    "\nLIST of CODE CHALLENGES\n",

    "\n\n*PRINT STATEMENTS*\n",
    "\nCODE CHALLENGE 1: Diamond",
    "\nDescription: \n",

    "\nCODE CHALLENGE 2: Name inside a diamond",
    "\nDescription: \n",

    "\nCODE CHALLENGE 3: Biodata",
    "\nDescription: simulates a biodata. very long program, and often times very annoying during testing.\n",

    "\n\n*OPERATORS*\n",
    "\nCODE CHALLENGE 4: Python operators",
    "\nDescription: uses the different python operators to calculate two inputs.\n",

    "\nCODE CHALLENGE 5: Fahrenheit to celsius",
    "\nDescription: exactly what you think it would do.\n",

    "\n\n*IF ELSE STATEMENTS*\n",
    "\nCODE CHALLENGE 6: Average grades",
    "\nDescription: totals your final grades and into your average grade.\n",

    "\nCODE CHALLENGE 7: Order something something whatever it was called simulator",
    "\nDescription: allows you to simulate logging your orders and calculating your total expenses.\n",

    "\n\n*LOOP STATEMENTS*\n",
    "\nCODE CHALLENGE 8: Sum of 10 numbers",
    "\nDescription: asks for 10 numbers and adds them.\n",

    "\nCODE CHALLENGE 9: Mirrored upside down triangle",
    "\nDescription: creates a mirrored upside down triangle with a size proportionate to user input.\n",

    "\nCODE CHALLENGE 10: Dynamic diamond",
    "\nDescription: creates a diamond with a size proportionate to user input.\n",

    "\nCODE CHALLENGE 11: Modified dynamic diamond",
    "\nDescription: honestly its the same thing..\n",

    "\nCODE CHALLENGE 12: Arrow",
    "\nDescription: creates an arrow.\n",

    "\nCODE CHALLENGE 13: Number diamond",
    "\nDescription: allows you to create a diamond made of numbers.... cool.... right?\n",

    "\nCODE CHALLENGE 14: While loop sum of all numbers",
    "\nDescription: continuously asks for a number and sums them all up when user types '0'\n",

    "\nCODE CHALLENGE 15: While loop triangles",
    "\nDescription: continuously asks the user if they want to add a triangle in a row.\n",

    "\nCODE CHALLENGE 16: Bank simulator",
    "\nDescription: simulates a bank. prepare an initial deposit of 10000.\n",

    )

def exinf():
    print(
    "\nLIST of EXTRAS\n",

    "\nEXTRA 1: Encoder",
    "\nDescription: encodes a number into a specific cipher's formula. useless unless modified.\n",

    "\nEXTRA 2: Binary",
    "\nDescription: converts numbers into binary. useful in itps.\n",

    "\nEXTRA 3: Char filter test program",
    "\nDescription: a test program for developing the filter feature of this compiler.\n",

    "\nEXTRA 4: Char filter",
    "\nDescription: the final product of the filter feature.\n",
    )

def help():
    print(
    "\nLIST\n",

    "\nACTIVITIES (1-25)",
    "\ntype 'act(number)' to access any specific activities.",
    "\ntype 'act info' or '1' for more info.\n",

    "\nCODE CHALLENGES (1-16)",
    "\ntype 'cc(number)' to access any specific code challenges.",
    "\ntype 'cc info' or '2' for more info.\n",

    "\nEXTRAS (1-4)",
    "\ntype 'ex(number)' to access any specific extras.",
    "\ntype 'ex info' or '3' for more info.\n",

    "\nSETTINGS",
    "\nmaybe you want to return to menu? (why would you?), type 'menu' if so."
    "\notherwise, type exit or 0 to quit.\n"
    )
help()
program=True



action = input("type which action you want to proceed with: ")
while program:

    num=1
    if action.lower()== "exit" or action.lower()=="quit" or action=="0":
        os.system('cls')
        print("bye")
        break
        
    elif action.lower()=="help":
        os.system('cls')
        help()
    elif action.lower()=="":
        os.system('cls')
        print("received no input. opening the 'help' tab instead.")
        help()
    elif action.lower()=="menu":
        os.system('cls')
        menuinf()
    elif action.lower()=="cc info" or action =="2":
        os.system('cls')
        ccinf()
    elif action.lower()=="act info" or action =="1":
        os.system('cls')
        actinf()
    elif action.lower()=="ex info" or action =="3":
        os.system('cls')
        exinf()

    ##CODE CHALLENGES
    elif action.lower()=="cc1":
        os.system('cls')
        ccn(action)
        cc1()

        end()
        
    elif action.lower()=="cc2":
        os.system('cls')
        ccn(action)
        cc2()

        end()

    elif action.lower()=="cc3":
        os.system('cls')
        intnotice()
        ccn(action)
        cc3()

        end()
        
    elif action.lower()=="cc4":
        os.system('cls')
        intnotice()
        ccn(action)
        cc4()

        end()
        
    elif action.lower()=="cc5":
        os.system('cls')
        intnotice()
        ccn(action)
        cc5()

        end()
        
    elif action.lower()=="cc6":
        os.system('cls')
        intnotice()
        ccn(action)
        cc6()

        end()
        
    elif action.lower()=="cc7":
        os.system('cls')
        intnotice()
        ccn(action)
        cc7()

        end()
        
    elif action.lower()=="cc8":
        os.system('cls')
        intnotice()
        ccn(action)
        cc8()

        end()
        
    elif action.lower()=="cc9":
        os.system('cls')
        intnotice()
        ccn(action)
        cc9()

        end()
        
    elif action.lower()=="cc10":
        os.system('cls')
        intnotice()
        ccn(action)
        cc10()

        end()
        
    elif action.lower()=="cc11":
        os.system('cls')
        intnotice()
        ccn(action)
        cc11()

        end()
        
    elif action.lower()=="cc12":
        os.system('cls')
        ccn(action)
        cc12()

        end()
        
    elif action.lower()=="cc13":
        os.system('cls')
        intnotice()
        ccn(action)
        cc13()

        end()
        
    elif action.lower()=="cc14":
        os.system('cls')
        intnotice()
        ccn(action)
        cc14()

        end()
        
    elif action.lower()=="cc15":
        os.system('cls')
        intnotice()
        ccn(action)
        cc15()

        end()
        
    elif action.lower()=="cc16":
        os.system('cls')
        intnotice()
        ccn(action)
        cc16()

        end()

    ##ACTIVITIES
    elif action.lower()=="act1":
        os.system('cls')
        actn(action)
        act1()

        end()
    elif action.lower()=="act2":
        os.system('cls')
        intnotice()
        actn(action)
        act2()

        end()
    elif action.lower()=="act3":
        os.system('cls')
        intnotice()
        actn(action)
        act3()

        end()
    elif action.lower()=="act4":
        os.system('cls')
        intnotice()
        actn(action)
        act4()

        end()
    elif action.lower()=="act5":
        os.system('cls')
        intnotice()
        actn(action)
        act5()

        end()
    elif action.lower()=="act6":
        os.system('cls')
        actn(action)
        act6()

        end()
    elif action.lower()=="act7":
        os.system('cls')
        intnotice()
        actn(action)
        act7()

        end()
    elif action.lower()=="act8":
        os.system('cls')
        actn(action)
        act8()

        end()
    elif action.lower()=="act9":
        os.system('cls')
        intnotice()
        actn(action)
        act9()

        end()
    elif action.lower()=="act10":
        os.system('cls')
        intnotice()
        actn(action)
        act10()

        end()
    elif action.lower()=="act11":
        os.system('cls')
        actn(action)
        act11()

        end()
    elif action.lower()=="act12":
        os.system('cls')
        intnotice()
        actn(action)
        act12()

        end()
    elif action.lower()=="act13":
        os.system('cls')
        actn(action)
        act13()

        end()
    elif action.lower()=="act14":
        os.system('cls')
        actn(action)
        act14()

        end()
    elif action.lower()=="act15":
        os.system('cls')
        actn(action)
        act15()

        end()
    elif action.lower()=="act16":
        os.system('cls')
        intnotice()
        actn(action)
        act16()

        end()
    elif action.lower()=="act17":
        os.system('cls')
        intnotice()
        actn(action)
        act17()

        end()
    elif action.lower()=="act18":
        os.system('cls')
        actn(action)
        act18()

        end()
    elif action.lower()=="act19":
        os.system('cls')
        intnotice()
        actn(action)
        act19()

        end()
    elif action.lower()=="act20":
        os.system('cls')
        actn(action)
        act20()

        end()
    elif action.lower()=="act21":
        os.system('cls')
        actn(action)
        act21()

        end()
    elif action.lower()=="act22":
        os.system('cls')
        actn(action)
        act22()

        end()
    elif action.lower()=="act23":
        os.system('cls')
        actn(action)
        act23()

        end()
    elif action.lower()=="act24":
        os.system('cls')
        actn(action)
        act24()

        end()
    elif action.lower()=="act25":
        os.system('cls')
        actn(action)
        act25()

        end()
    ##EXTRAS
        end()
    elif action.lower()=="ex1":
        os.system('cls')
        intnotice()
        exn(action)
        encoder()

        end()
    elif action.lower()=="ex2":
        os.system('cls')
        intnotice()
        exn(action)
        binary()

        end()
    elif action.lower()=="ex3":
        os.system('cls')
        exn(action)
        filtertest()

        end()
    elif action.lower()=="ex4":
        os.system('cls')
        exn(action)

        f()

        end()

    

    else:
        os.system('cls')
        print(f"input unrecognized.. there is no such thing as {action}. unless it's a misinput?")

    action = input("type which action you want to proceed with. if in need of instructions, type 'help': ")
    
    