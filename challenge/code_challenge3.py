def cc():
 print("INFO: code_challenge3 is a biodata simulation program, similar to activity3. please input the appropriate datas, as there will be a twist in the end for no absolute reason.\n")
 name = input("\nEnter name: ")

 num = int(input("\nEnter number: "))

 mail = input("\nEnter email: ")

 gender = input("\nEnter gender: ")

 age = int(input("\nEnter age: "))

 bday = input("\nEnter Birthdate: ")

 status = input("\nAre you married? (YES or NO): ")

 religion = input("\nEnter religion: ")

 nation = input("\nEnter nationality: ")

 workplace = input("\nEnter workplace: ")

 address = input("\nEnter address: ")

 father = input("\nEnter Father's name: ")

 mother = input("\nEnter Mother's name: ")

 smoke = input("\nDo you smoke? (YES or NO): ")

 drink = input("\nDo you drink? (YES or NO): ")

 morning = input("\nWhat do you drink every morning?: ")

 stretch = int(input("\nHow long does it take you to stretch before bed time? (in minutes): "))

 hometime = int(input("\nWhat time do you generally get home? (24 hour format): "))

 bedtime = int(input("\nWhat time do you generally go to bed? (24 hour format): "))

 sleep = input("\nDo you make sure you get 8 hours of sleep? (YES or NO): ")

 sleepissues = input("\nDo you have problems sleeping until morning? (YES or NO): ")

 baby = input("\nDo you experience fatigue and stress whenever you wake up in the morning? (YES or NO): ")

 checkup = input("\nWere you diagnosed with issues in your last check-up? (YES or NO): ")



 if hometime > 24:
  hometime = 12
  timeh = "AM"
 elif hometime > 12:
  hometime = hometime - 12
  timeh = "PM"
 else:
  timeh = "AM"

 if bedtime > 24:
  bedtime = 12
  timeb = "AM"
 elif bedtime > 12:
  bedtime = bedtime - 12
  timeb = "PM"
 else:
  timeb = "AM"


 if smoke.lower() == "yes":
  smoke = "do"
 else:
  smoke = "dont"


 if drink.lower() == "yes":
  drink = "i do"
 else:
  drink = "i dont"


 if status.lower() == "yes":
  married = "currently"
 else:
  married = "not"
  status = "no"


 if sleep.lower() == "no":
  sleep = "generally dont care if i get"
 else:
   sleep = "make sure I get"

 if sleepissues.lower() == "yes":
  sleepissues = "usually still encounter"
 else:
  sleepissues = "usually have no"

 if baby.lower() == "no":
  baby = "a baby, I wake up without any fatigue or stress in the morning."
 else:
   baby = "a crooked elder in his 80s, i wake up with fatigue and/or stress in the morning."

 if checkup.lower() == "yes":
  checkup = "I was a mess"
 else:
  checkup = "there were no issues"


 print("\n\nDONE!\nWELCOME TO THE YOSHIKAGE KIRA BIOGRAPHY COPYPASTA. HERE IS YOUR RESULT: ")



 print("\nMy name is " ,name,". I'm " ,age, " years old. My house is in " ,address, " where all the villas are, and " ,status.lower(), ", I am " ,married, "a married" ,nation, ". my email is " ,mail, ", and I work as an employee for " ,workplace, ". You can call me anytime using my number: " ,num, ". I am a devoted " ,religion, ", and I get home every day by " ,hometime , timeh, " at the latest. My father's name is " ,father, ", and my mother's name is " ,mother, ". I ",smoke," smoke, ",drink," drink, and I'm in bed by " ,bedtime , timeb, ". I " ,sleep, " eight hours of sleep, no matter what. After having a glass of warm ",morning," and doing about ",stretch," minutes of stretches before going to bed, I" ,sleepissues, " problems sleeping until morning. Just like " ,baby, " I was told " ,checkup, " at my last check-up. I'm trying to explain that I'm a person who wishes to live a very quiet life. I take care not to trouble myself with any enemies, like winning and losing, that would cause me to lose sleep at night. That is how I deal with society, and I know that is what brings me happiness. Although, if I were to fight I wouldn't lose to anyone.")