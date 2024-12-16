def cc():
    print("INFO: code_challenge6 is a program that asks for your overall grades for the following questions.\n")
    name = input ("enter your name: ")

    print("enter your grades on the following (70-100 only).\n")

    prelim = input("enter your prelim's grades: ")
    midterm = input("enter your midterm's grades: ")
    semi = input("enter your semi-final's grades: ")
    final = input("enter your final's grades: ")
    quiz = input("enter your total quiz grades: ")
    project = input("enter your projects' grades: ")


    """FILTER CODE THAT IM VERY PROUD I MADE"""
    echo=prelim
    echo1=midterm
    echo2=semi
    echo3=final
    echo4=quiz
    echo5=project
    keep= "1234567890"
    for filterer in keep.lower(): 
        prelim = prelim.lower().replace(filterer,'')
        midterm = midterm.lower().replace(filterer,'')
        semi = semi.lower().replace(filterer,'')
        final = final.lower().replace(filterer,'')
        quiz = quiz.lower().replace(filterer,'')
        project = project.lower().replace(filterer,'')
    for converter in prelim:
        echo= echo.lower().replace(converter,'')
        if echo == "":
            echo="0"
    for converter in midterm:
        echo1= echo1.lower().replace(converter,'')
        if echo1 == "":
            echo1="0"
    for converter in semi:
        echo2= echo2.lower().replace(converter,'')
        if echo2 == "":
            echo2="0"
    for converter in final:
        echo3= echo3.lower().replace(converter,'')
        if echo3 == "":
            echo3="0"
    for converter in quiz:
        echo4= echo4.lower().replace(converter,'')
        if echo4 == "":
            echo4="0"
    for converter in project:
        echo5= echo5.lower().replace(converter,'')
        if echo5 == "":
            echo5="0"

    prelim=int(echo)
    midterm=int(echo1)
    semi=int(echo2)
    final=int(echo3)
    quiz=int(echo4)
    project=int(echo5)
    """END OF THE FILTER CODE THAT IM VERY PROUD TO HAVE MADE"""





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
