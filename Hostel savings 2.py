print("Welcome to spartan saving, where saving is spartaculous.")
Spartans = {"Sekyim":{"pin":"1432", "balance":900000.0},
            "Alex":{"pin":"3512", "balance": 300.5},
            "Julie":{"pin":"1198", "balance": 29.8}
}
user_pin=input("Enter your 4 digit pin:")
for name, pin in Spartans.items():
    #print(pin["pin"])
    if user_pin==pin["pin"]:
        print(f"Hello {name},what would you like to do today")
        while True:     
         print("1. Check Balance")
         print("2. Deposit")
         print("3. Withdraw")
         print("4. Exit")
         option=input("Enter option number:")
         if option=="1":
           print(pin["balance"])
         elif option=="2":
            amount=float(input("enter amount:"))
            pin["balance"]+=amount
            print(f"your new balance is {pin['balance']}")
         elif option== "3":
            withdraw = float(input("How much do you want to withdraw?\n"))
            if withdraw <= pin["balance"]:
                pin["balance"] -= withdraw
                print(f"Withdrawal successful! Your new balance is {pin['balance']}\n")
            else:
                print("Insufficient funds!")
         elif option=="4":
            print("Thanks for using spartaculus saving bank!")
            break
         else:
             print("Invalid option, please try again.")
        break
else:
       print("invalid pin")

    
    

    
    