name = input("enter your name: ")

password = input("\nenter your password: ")

if password == "gwapito123" and name.lower() == "sean":

 print(f"\nwelcome gwapo.")

elif password == "poper" and name.lower() == "reaper":

 print(f"\nwelcome {name}.")

else:
 print("\npassword does not match account name or account doesnt exist.")
