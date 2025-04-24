import random
import sys
from getpass import getpass

# Observer Pattern
class AccountObserver:
    def update(self, message):
        print(f"\n📢 Notification: {message}\n")

# Strategy Pattern
class AccountType:
    def interest_rate(self):
        pass

class SavingsAccount(AccountType):
    def interest_rate(self):
        return 4

class CurrentAccount(AccountType):
    def interest_rate(self):
        return 0

# Memento Pattern
class Memento:
    def __init__(self, transactions):
        self.transactions = transactions.copy()

# Main ATM Class
class ATM:
    def __init__(self, name, account_number, balance=0, account_type=None):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type
        self.observers = []
        self.transactions = []

    # Observer Methods
    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, message):
        for observer in self.observers:
            observer.update(message)

    # Core Functionalities
    def check_balance(self):
        print("\n----------ACCOUNT DETAIL----------")
        print(f"Account Holder: {self.name.upper()}")
        print(f"Account Number: {self.account_number}")
        print(f"Available Balance: INR {self.balance}\n")

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited: INR {amount}")
        self.notify_observers(f"Deposited INR {amount}. New Balance: INR {self.balance}")
        print(f"✅ Current account balance: INR {self.balance}\n")

    def withdraw(self, amount):
        if amount > self.balance:
            print("❌ Insufficient fund!")
            print(f"Your balance is INR {self.balance} only.\n")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrawn: INR {amount}")
            self.notify_observers(f"Withdrawn INR {amount}. Remaining Balance: INR {self.balance}")
            print(f"✅ INR {amount} withdrawal successful!")
            print(f"Current account balance: INR {self.balance}\n")

    def transfer_amount(self, amount):
        if amount > self.balance:
            print("❌ Insufficient fund!")
            print(f"Your balance is INR {self.balance} only.\n")
        else:
            self.balance -= amount
            self.transactions.append(f"Transferred: INR {amount}")
            self.notify_observers(f"Transferred INR {amount}. Remaining Balance: INR {self.balance}")
            print(f"✅ INR {amount} transfer successful!")
            print(f"Current account balance: INR {self.balance}\n")

    def calculate_interest(self):
        if self.account_type:
            rate = self.account_type.interest_rate()
            interest = (self.balance * rate) / 100
            print(f"📈 Annual Interest Earned: INR {interest}\n")
        else:
            print("No account type specified.\n")

    # Memento Methods
    def save_state(self):
        return Memento(self.transactions)

    def restore_state(self, memento):
        self.transactions = memento.transactions
        print("\n📜 Transaction history restored.\n")

    # CLI Menu
    def transaction(self):
        print("""
            TRANSACTION 
        *********************
            Menu:
            1. Check Balance
            2. Deposit
            3. Withdraw
            4. Transfer money
            5. View Interest
            6. View Transaction History
            7. Exit
        *********************""")

        while True:
            try:
                option = int(input("Enter 1-7: "))
            except:
                print("⚠️ Error: Please enter a number between 1 and 7!\n")
                continue

            if option == 1:
                self.check_balance()
            elif option == 2:
                amount = int(input("Enter deposit amount (INR): "))
                self.deposit(amount)
            elif option == 3:
                amount = int(input("Enter withdrawal amount (INR): "))
                self.withdraw(amount)
            elif option == 4:
                amount = int(input("Enter transfer amount (INR): "))
                self.transfer_amount(amount)
            elif option == 5:
                self.calculate_interest()
            elif option == 6:
                print("\n🧾 Transaction History:")
                for t in self.transactions:
                    print(f" - {t}")
                print()
            elif option == 7:
                print("""
                Printing receipt..............
          ******************************************
              Transaction is now complete.                                             
              Thanks for choosing us as your bank.                  
          ******************************************
                """)
                break
            else:
                print("⚠️ Invalid choice. Please try again.\n")


# Main Driver Code
print("*******WELCOME TO BANK OF PAKISTAN*******")
print("___________________________________________________________\n")
pin1 = getpass("Enter your 4-digit PIN: ")
pin2 = getpass("Re-enter your 4-digit PIN: ")

if pin1 == pin2:
    print("\n----------ACCOUNT DETAILS----------")
    name = input("Enter your name: ")
    account_number = input("Enter your account number: ")
    
    # Choose account type dynamically
    print("\nChoose Account Type:")
    print("1. Savings Account (4% Interest)")
    print("2. Current Account (0% Interest)")
    acc_choice = input("Enter 1 or 2: ")
    
    if acc_choice == "1":
        account_type = SavingsAccount()
    else:
        account_type = CurrentAccount()

    atm = ATM(name, account_number, account_type=account_type)
    observer = AccountObserver()
    atm.add_observer(observer)

    print("🎉 Congratulations! Account created successfully...\n")

    while True:
        trans = input("Do you want to do any transaction? (y/n): ").lower()
        if trans == "y":
            atm.transaction()
        elif trans == "n":
            print("""
        -------------------------------------
    | Thanks for choosing us as your bank |
    | Visit us again!                     |
        -------------------------------------""")
            break
        else:
            print("❌ Invalid input. Please enter 'y' or 'n'.\n")
else:
    print("❌ PINs do not match. Please try again.")
