def cc():
 print("INFO: code_challenge7 is a simulation of that thing that takes your order (i forgot the name).\n")
 print("this program is really long and annoying. if you wish to quit, type 0. otherwise, type enter.")
 annoying=input("")
 if annoying == "0":
  print("so relatable")
 else:
  name = input("enter your name: ")
  age = eval(input("enter your age: "))
  ask = input("did you buy grocery (yes or no): ")

  ################################################################
  disc = "INACTIVE"
  if age > 59:
    disc = "ACTIVE"
  ################################################################
  c=0
  if ask.lower() == "yes":
    print(
    "\nokay, here is a list of our grocery items:",
    "\n(A) corn kernel - 1 peso",
    "\n(B) grain of rice - 0.1 peso",
    "\n(C) dung - 999 pesos",
    "\n\nkeep in mind that you are eligible for a 5.2% discount if you are at the age of 60 or above.",
    f"\nDISCOUNT STATUS: {disc}",
    )

  #####################################
    
  #####################################
    order = input("\nplease enter your purchased item's ID: ")
    print(f"you have ordered item {order}.")
    amount = eval(input("\nlastly, please input the amount of money paid: "))
    print(f"you handed {amount} pesos.")
  
    if order.lower() == "a":
      c+=1
    elif order.lower() == "b":
      c+=0.1
    elif order.lower() == "c" :
      c+=999
    total = amount-c
    
    if age > 59 :
      
      print(
      f"\nyour change would be {total} pesos in its very base.",

      f"\n\nMONEY PAID: {amount}",
      f"\nDISCOUNTED ITEM PRICE ({order}): {c-(c*0.052)} (5.2%)",
      f"\nTAX: {c*0.123} (12.3% inflation)",
      f"\nTOTAL: {(amount-(c-(c*0.052)))-(c*0.123)}",

      f"\nyour change would be {(amount-(c-(c*0.052)))-(c*0.123)} pesos in total. eligibility for discount has reduced the price by 5.2%, followed by a 12.3% tax deduction.")

    else:

      print(
      f"\nyour change would be {total} pesos in its very base.",

      f"\n\nMONEY PAID: {amount}",
      f"\nTAX: {c*0.123} (12.3% inflation)",
      f"\nTOTAL: {(amount-c)-(c*0.123)}",

      f"\nyour change would be {(amount-c)-(c*0.123)} pesos in total, followed by a 12.3% tax deduction.")
  #####################################################################

  elif ask.lower() == "no":
    print("ok")
  else:
    print("input cannot be recognized. please make sure the input is one of the following options (yes/no).")

cc()