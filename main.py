import time
import json
from rich import print
from rich.table import Table

def show_transactions(transactions):
    table = Table(title = "Your transactions")
    table.add_column("Description")
    table.add_column("Amount")
    for transaction in transactions:
        table.add_row(transaction['description'], str(transaction['amount']))
    print(table)

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
    print("Options:\n1. Make a transaction\n2. View transactions\n3. Leave")
    time.sleep(1)
    choice = input("What option would you like to proceed with: ").lower()

    if choice in ("1", "make a transaction"):
        description = str(input("Enter the description of your transaction (e.g food): "))
        amount = float(input("Enter the amount of your transaction (e.g 2.50): £ "))
        print(f"You have requested a transaction of £{amount} for {description}.")
        transactions.append({"description" : description, "amount" : amount})
        save_transactions(transactions)

    elif choice in ("2", "view transactions"):
        show_transactions(transactions)

    elif choice in ("3", "leave"):
        confirm = input("Are you sure you want to leave (Y/N): ").lower()

        if confirm in ("y", "yes"):
            print("Goodbye, heres an overview of your transactions: ")   
            show_transactions(transactions)
            break
            
        else:
            time.sleep(1)
            print("Returning to menu...")
        
    else:
        time.sleep(1)
        print("Please enter a valid option, 1, 2 or 3!")   


