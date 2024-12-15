def act():
 name = input("enter your name, dear miner: ")
 gold = 0
 isgold = input("\ndo you own a piece of gold? (YES or NO): ")
 
 if isgold.lower() == "yes":
  gold += 1
  ismanygold = input(f"\ndang thats cool. you have {gold} gold then? (YES or NO): ")
 
  if ismanygold.lower() == "no":
   gold = eval(input(f"\nyou own more than {gold} gold? then how much do you own? (enter a number): "))
 
   if gold > 1:
    print(f"\ni see. thats a lot of gold {name}.")
   elif gold == 1:
    print("\nso you do have one gold after all.")
   else:
    print(f"\nstop messing with me {name}!")
  else:
   print(f"\nthats cool {name}! i hope you treasure your gold.")

 else:
  print(f"\nyou have {gold} gold? you broke as hell {name}.")
