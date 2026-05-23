import time
import json

def save_transactions(transactions):
    with open("budget.json", "w") as f:
        json.dump(transactions, f)

def load_transactions():
    try:
        with open("budget.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return[]
    except json.JSONDecodeError:
        return[]    
    
transactions = load_transactions()

while True:

    print("\n===Budget Tracker===")
    time.sleep(1)
    print("Options:\n1. Transaction\n2. Leave")
    time.sleep(1)
    choice = input("What option would you like to proceed with: ").lower()

    if choice == "1":
        description = str(input("Enter the description of your transaction (e.g food): "))
        amount = float(input("Enter the amount of your transaction (e.g 2.50): £ "))
        print(f"You have requested a transaction of £{amount} for {description}.")
        transactions.append({"description" : description, "amount" : amount})
        save_transactions(transactions)

    elif choice == "2":
        confirm = input("Are you sure you want to leave (Y/N): ").lower()

        if confirm == "y":
            print("Goodbye, heres an overview of your transactions: ")
            for transaction in transactions:
                print(f"{transaction['description']} - £{transaction['amount']}")
            break

        else:
            print("Returning to menu...")
        
    else:
        print("Please enter a valid option, 1 or 2!")   
        
        


