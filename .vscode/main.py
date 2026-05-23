import json
transactions = []

while True:

    print("\n===Budget Tracker===")
    print("Options:\n1. Transaction\n2. Leave")
    choice = input("What option would you like to proceed with: ").lower()

    if choice == "1":
        description = str(input("Enter the description of your transaction (e.g food): "))
        amount = float(input("Enter the amount of your transaction (e.g 2.50): £ "))
        print(f"You have requested a transaction of £{amount} for {description}.")
        transactions.append({"description" : description, "amount" : amount})

    elif choice == "2":
        confirm = input("Are you sure you want to leave (Y/N): ").lower()

        if confirm == "y":
            print("Goodbye!")
            break

        else:
            print("Returning to menu...")
        
    else:
        int(input("Please enter a valid number: "))   
        
        


