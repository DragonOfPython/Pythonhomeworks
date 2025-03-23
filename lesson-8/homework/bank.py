import json
import os

class Account:
    def __init__(self, account_number, name, initial_deposit):
        self.account_number = account_number
        self.name = name
        self.balance = initial_deposit

    def to_dict(self):
        """Convert account information to dictionary for JSON serialization."""
        return {
            "account_number": self.account_number,
            "name": self.name,
            "balance": self.balance
        }

class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()

    def generate_account_number(self):
        """Generate a unique account number."""
        return str(len(self.accounts) + 1)  # Simple sequential account number

    def create_account(self, name, initial_deposit):
        """Create a new account."""
        if initial_deposit < 0:
            print("Initial deposit cannot be negative.")
            return
        account_number = self.generate_account_number()
        new_account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = new_account
        self.save_to_file()
        print(f"Account created successfully! Account Number: {account_number}")

    def view_account(self, account_number):
        """View account details."""
        account = self.accounts.get(account_number)
        if account:
            print(f"Account Number: {account.account_number}")
            print(f"Name: {account.name}")
            print(f"Balance: {account.balance}")
        else:
            print("Account not found.")

    def deposit(self, account_number, amount):
        """Deposit money into account."""
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        account = self.accounts.get(account_number)
        if account:
            account.balance += amount
            self.save_to_file()
            print(f"{amount} deposited successfully. New balance: {account.balance}")
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        """Withdraw money from account."""
        account = self.accounts.get(account_number)
        if account:
            if amount > account.balance:
                print("Insufficient funds.")
            elif amount <= 0:
                print("Withdrawal amount must be positive.")
            else:
                account.balance -= amount
                self.save_to_file()
                print(f"{amount} withdrawn successfully. New balance: {account.balance}")
        else:
            print("Account not found.")

    def save_to_file(self):
        """Save account details to a file."""
        with open('accounts.txt', 'w') as file:
            json.dump({number: account.to_dict() for number, account in self.accounts.items()}, file)

    def load_from_file(self):
        """Load account details from a file."""
        if os.path.exists('accounts.txt'):
            with open('accounts.txt', 'r') as file:
                accounts_data = json.load(file)
                for account_number, account_info in accounts_data.items():
                    account = Account(
                        account_info['account_number'],
                        account_info['name'],
                        account_info['balance']
                    )
                    self.accounts[account_number] = account

def main():
    bank = Bank()
    
    while True:
        print("\nWelcome to the Bank Application!")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            initial_deposit = float(input("Enter initial deposit: "))
            bank.create_account(name, initial_deposit)

        elif choice == "2":
            account_number = input("Enter account number: ")
            bank.view_account(account_number)

        elif choice == "3":
            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            bank.deposit(account_number, amount)

        elif choice == "4":
            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            bank.withdraw(account_number, amount)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()