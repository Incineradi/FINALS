def cc():
    print("INFO: code_challenge6 is a program that asks for your overall grades for the following questions.\n")
    name = input ("enter your name: ")

    print("enter your grades on the following (70-100 only).\n")

    prelim = eval(input("enter your prelim's grades: "))
    midterm = eval(input("enter your midterm's grades: "))
    semi = eval(input("enter your semi-final's grades: "))
    final = eval(input("enter your final's grades: "))
    quiz = eval(input("enter your total quiz grades: "))
    project = eval(input("enter your projects' grades: "))

    if (prelim or midterm or semi or final or quiz or project) < 70 or (prelim or midterm or semi or final or quiz or project) > 100 :
        print("invalid number detected.")

    else:
        grade = (prelim*0.15)+(midterm*0.15)+(semi*0.15)+(final*0.15)+(quiz*0.25)+(project*0.15)
    #just incase
    if grade > 100 or grade < 70:
        print("\ninvalid numbers.")
    
    elif grade == 100:
        print("you're lying.")
    elif grade > 74:
        print(f"\ncongratulations {name}. you passed the subject with a total grade of {round(grade,0)}.")

    else:
        print(f"\n{round(grade,0)}??????? you failed bruh what the hell")








