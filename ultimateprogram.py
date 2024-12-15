import os
##import cc
from challenge.code_challenge1 import cc as cc1
from challenge.code_challenge2 import cc as cc2
##from challenge.code_challenge3 import cc as cc3
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
##from activity.activity1 import act as act1
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
from extras.ENCODER import encoder as enc


"""people tell me these blocks of import look ugly but honestly they're so pretty to look at"""


os.system('cls')
def end():
    print("simulation ended.")
##for calling
def ccn(c):
    print(f"successfully imported code_challenge{c[2]}")

def actn(c):
    print(f"successfully imported activity{c[3]}")

def tn(c):
    print(f"successfully imported code_challenge{c[2]}")
    
def help():
    print(
    "\nLIST\n",

    "\nACTIVITIES (1-25)",
    "\ntype 'act(number)' to access any specific activities.",
    "\ntype 'act info' for more info.\n",

    "\nCODE CHALLENGES (1-16)",
    "\ntype 'cc(number)' to access any specific code challenges.",
    "\ntype 'cc info' for more info.\n",

    "\notherwise, type exit or 0 to quit.\n"
    )
help()
program=True





while program:

    num=1
    action = input("type which action you want to proceed with. if in need of instructions, type 'help': ")
    if action.lower()== "exit" or action.lower()=="quit" or action=="0":
        os.system('cls')
        print("bye")
        
    elif action.lower()=="help":
        os.system('cls')
        help()

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

    ###################################################################
    elif action.lower()=="cc3":
        os.system('cls')
        ccn(action)
        ##cc3()

        end()
        
        #############################################################
    elif action.lower()=="cc4":
        os.system('cls')
        ccn(action)
        cc4()

        end()
        
    elif action.lower()=="cc5":
        os.system('cls')
        ccn(action)
        cc5()

        end()
        
    elif action.lower()=="cc6":
        os.system('cls')
        ccn(action)
        cc6()

        end()
        
    elif action.lower()=="cc7":
        os.system('cls')
        ccn(action)
        cc7()

        end()
        
    elif action.lower()=="cc8":
        os.system('cls')
        ccn(action)
        cc8()

        end()
        
    elif action.lower()=="cc9":
        os.system('cls')
        ccn(action)
        cc9()

        end()
        
    elif action.lower()=="cc10":
        os.system('cls')
        ccn(action)
        cc10()

        end()
        
    elif action.lower()=="cc11":
        os.system('cls')
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
        ccn(action)
        cc13()

        end()
        
    elif action.lower()=="cc14":
        os.system('cls')
        ccn(action)
        cc14()

        end()
        
    elif action.lower()=="cc15":
        os.system('cls')
        ccn(action)
        cc15()

        end()
        
    elif action.lower()=="cc16":
        os.system('cls')
        ccn(action)
        cc16()

        end()
    ##ACTIVITIES
    elif action.lower()=="act1":
        os.system('cls')
        ccn(action)
        cc16()

        end()
    elif action.lower()=="act1":
        os.system('cls')
        ccn(action)
        act1()

        end()
    elif action.lower()=="act2":
        os.system('cls')
        ccn(action)
        act2()

        end()
    elif action.lower()=="act3":
        os.system('cls')
        ccn(action)
        act3()

        end()
    elif action.lower()=="act4":
        os.system('cls')
        ccn(action)
        act4()

        end()
    elif action.lower()=="act5":
        os.system('cls')
        ccn(action)
        act5()

        end()
    elif action.lower()=="act6":
        os.system('cls')
        ccn(action)
        act6()

        end()
    elif action.lower()=="act7":
        os.system('cls')
        ccn(action)
        act7()

        end()
    elif action.lower()=="act8":
        os.system('cls')
        ccn(action)
        act8()

        end()
    elif action.lower()=="act9":
        os.system('cls')
        ccn(action)
        act9()

        end()
    elif action.lower()=="act10":
        os.system('cls')
        ccn(action)
        act10()

        end()
    elif action.lower()=="act11":
        os.system('cls')
        ccn(action)
        act11()

        end()
    elif action.lower()=="act12":
        os.system('cls')
        ccn(action)
        act12()

        end()
    elif action.lower()=="act13":
        os.system('cls')
        ccn(action)
        act13()

        end()
    elif action.lower()=="act14":
        os.system('cls')
        ccn(action)
        act14()

        end()
    elif action.lower()=="act15":
        os.system('cls')
        ccn(action)
        act15()

        end()
    elif action.lower()=="act16":
        os.system('cls')
        ccn(action)
        act16()

        end()
    elif action.lower()=="act17":
        os.system('cls')
        ccn(action)
        act17()

        end()
    elif action.lower()=="act18":
        os.system('cls')
        ccn(action)
        act18()

        end()
    elif action.lower()=="act19":
        os.system('cls')
        ccn(action)
        act19()

        end()
    elif action.lower()=="act20":
        os.system('cls')
        ccn(action)
        act20()

        end()
    elif action.lower()=="act21":
        os.system('cls')
        ccn(action)
        act21()

        end()
    elif action.lower()=="act22":
        os.system('cls')
        ccn(action)
        act22()

        end()
    elif action.lower()=="act23":
        os.system('cls')
        ccn(action)
        act23()

        end()
    elif action.lower()=="act24":
        os.system('cls')
        ccn(action)
        act24()

        end()
    elif action.lower()=="act25":
        os.system('cls')
        ccn(action)
        act25()

        end()
    ##EXTRAS
    elif action.lower()=="t1":
        os.system('cls')
        ccn(action)
        t1()

        end()
    elif action.lower()=="t2":
        os.system('cls')
        ccn(action)
        t2()

        end()
    elif action.lower()=="t3":
        os.system('cls')
        ccn(action)
        t3()

        end()
    elif action.lower()=="t4":
        os.system('cls')
        ccn(action)
        t4()

        end()
    elif action.lower()=="encoder":
        os.system('cls')
        ccn(action)
        enc()

        end()



    else:
        os.system('cls')
        print("input unrecognized..")
        
    
    