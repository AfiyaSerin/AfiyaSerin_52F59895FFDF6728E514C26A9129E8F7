class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited {amount}. New balance: {self.__account_balance}")
        else:
            print("Invalid amount. Deposit amount should be greater than 0.")

    def withdraw(self, amount):
        if amount > 0:
            if self.__account_balance >= amount:
                self.__account_balance -= amount
                print(f"Withdrawn {amount}. New balance: {self.__account_balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid amount. Withdrawal amount should be greater than 0.")

    def display_balance(self):
        print(f"Account balance: {self.__account_balance}")


# Testing the BankAccount class
account = BankAccount("123456789", "John Doe", 1000)
account.display_balance()  # Account balance: 1000

account.deposit(500)  # Deposited 500. New balance: 1500
account.withdraw(200)  # Withdrawn 200. New balance: 1300

account.display_balance()  # Account balance: 1300