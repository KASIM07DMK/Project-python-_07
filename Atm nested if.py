card=input("Do you have Atm Card? (yes/no):")

if card == "yes":
   pin = input("Enter your Pin:")

   if pin == "7890":
      print("your transaction is successfully completed...")

   else:
      print("you have entered incorrect pin...")

else:
   print("Enter your Atm card:")      