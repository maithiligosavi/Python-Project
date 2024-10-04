from datetime import datetime

class TrackTreasury:
    def __init__(self):
        self.balance = 0
        self.transactions = []

    def add_income(self, amount, description="Income"):
        if amount > 0:
            self.balance += amount
            self.transactions.append({
                "type": "Income", 
                "amount": amount, 
                "description": description,
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
            })
            print(f"Added income: {amount}. New balance: {self.balance}")
        else:
            print("Income amount must be greater than 0.")

    def add_expense(self, amount, description="Expense"):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                self.transactions.append({
                    "type": "Expense", 
                    "amount": amount, 
                    "description": description,
                    "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
                })
                print(f"Added expense: {amount}. New balance: {self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Expense amount must be greater than 0.")

    def show_balance(self):
        print(f"Current balance: {self.balance}")

    def show_transactions(self):
        if not self.transactions:
            print("No transactions yet.")
        else:
            print("Transaction History:")
            for i, transaction in enumerate(self.transactions, 1):
                print(f"{i}. {transaction['type']}: {transaction['amount']} ({transaction['description']}) [{transaction['date']}]")

# Example usage

tracker = TrackTreasury()

while True:
    print("\nTrack your treasury:")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Show Balance")
    print("4. Show Transactions")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        amount = float(input("Enter income amount: "))
        description = input("Enter a description (optional): ") or "Income"
        tracker.add_income(amount, description)

    elif choice == '2':
        amount = float(input("Enter expense amount: "))
        description = input("I spended on... (optional): ") or "Expense"
        tracker.add_expense(amount, description)

    elif choice == '3':
        tracker.show_balance()

    elif choice == '4':
        tracker.show_transactions()

    elif choice == '5':
        print("Exiting Budget Tracker. Spend wisely and have a great day!")
        break

    else:
        print("Invalid option. Please try again.")
