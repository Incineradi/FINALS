def act():
 print("INFO: activity3 is a biodata simulation program, similar to code_challenge3. please input the appropriate datas, and if asked for an integer, remember to only type numbers with no special characters, as there will be a twist in the end for no absolute reason.\n")
 print("this program is really long and annoying. if you wish to quit, type 0. otherwise, type enter.")
 annoying=input("")
 if annoying == "0":
  print("so relatable")
 else:
  name = input("\nEnter name: ")

  num = input("\nEnter number, whole number only: ")

  mail = input("\nEnter email: ")

  gender = input("\nEnter gender: ")

  age = input("\nEnter age, whole number only: ")

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

  stretch = input("\nHow long does it take you to stretch before bed time? (in minutes, whole number only): ")

  hometime = input("\nWhat time do you generally get home? (24 hour format, whole number only): ")

  bedtime = input("\nWhat time do you generally go to bed? (24 hour format, whole number only): ")

  sleep = input("\nDo you make sure you get 8 hours of sleep? (YES or NO): ")

  sleepissues = input("\nDo you have problems sleeping until morning? (YES or NO): ")

  baby = input("\nDo you experience fatigue and stress whenever you wake up in the morning? (YES or NO): ")

  checkup = input("\nWere you diagnosed with issues in your last check-up? (YES or NO): ")
  
  """FILTER CODE THAT IM VERY PROUD I MADE"""
  echo=num
  echo1=age
  echo2=stretch
  echo3=hometime
  echo4=bedtime
  keep= "1234567890"
  for filterer in keep.lower(): 
      num = num.lower().replace(filterer,'')
      age = age.lower().replace(filterer,'')
      stretch = stretch.lower().replace(filterer,'')
      hometime = hometime.lower().replace(filterer,'')
      bedtime = bedtime.lower().replace(filterer,'')
  for converter in num:
      echo= echo.lower().replace(converter,'')
      if echo == "":
        echo="0"
  for converter in age:
      echo1= echo1.lower().replace(converter,'')
      if echo1 == "":
        echo1="0"
  for converter in stretch:
      echo2= echo2.lower().replace(converter,'')
      if echo2 == "":
        echo2="0"
  for converter in hometime:
      echo3= echo3.lower().replace(converter,'')
      if echo3 == "":
        echo3="0"
  for converter in bedtime:
      echo4= echo4.lower().replace(converter,'')
      if echo4 == "":
        echo4="0"

  num=int(echo)
  age=int(echo1)
  stretch=int(echo2)
  hometime=int(echo3)
  bedtime=int(echo4)

  """END OF THE FILTER CODE THAT IM VERY PROUD TO HAVE MADE"""





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
