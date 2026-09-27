# Custom Exception for specific business logic errors
class InsufficientFundsError(Exception):
    pass


class BankAccount:
    # Constructor: Initializes the object state
    def __init__(self, account_holder, initial_balance=0.0):
        self.account_holder = account_holder
        # Encapsulation: Double underscore hides the variable from direct outside access
        self.__balance = float(initial_balance)
        self.transaction_history = []

    def deposit(self, amount):
        # 1. Built-in functions & Exception Handling
        if not isinstance(amount, (int, float)):
            raise TypeError("Deposit amount must be a number.")

        if amount <= 0:
            raise ValueError("Deposit amount must be strictly positive.")

        self.__balance += amount
        self.transaction_history.append(amount)
        print(f"Deposited ${amount:.2f} successfully.")

    def withdraw(self, amount):
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Withdrawal must be greater than zero.")
            if amount > self.__balance:
                raise InsufficientFundsError(f"Cannot withdraw ${amount}. Current balance is ${self.__balance}.")

            self.__balance -= amount
            # Recording as a negative number for history
            self.transaction_history.append(-amount)
            print(f"Withdrew ${amount:.2f} successfully.")

        # Catching specific errors prevents the whole program from crashing
        except ValueError as ve:
            print(f"Data Error: {ve}")
        except InsufficientFundsError as ife:
            print(f"Transaction Denied: {ife}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def get_account_summary(self):
        # Using built-in Python functions: sum(), max(), min(), len(), round()
        total_transactions = len(self.transaction_history)

        if total_transactions > 0:
            largest_deposit = max(self.transaction_history)
            # Filter out negative numbers to find the largest actual deposit
            largest_deposit = largest_deposit if largest_deposit > 0 else 0
        else:
            largest_deposit = 0

        print(f"\n--- Account Summary for {self.account_holder} ---")
        print(f"Current Balance: ${round(self.__balance, 2)}")
        print(f"Total Transactions: {total_transactions}")
        print(f"Largest Single Deposit: ${largest_deposit}")


# Execution and Testing
print("Initializing Bank System...")
account = BankAccount("John Doe", 500)

# Simulating operations
account.deposit(150.50)
account.withdraw(100)

# Triggering exceptions intentionally to show how they are handled safely
print("\n--- Testing Error Handling ---")
account.withdraw(9999)  # Triggers InsufficientFundsError
account.withdraw(-50)  # Triggers ValueError

account.get_account_summary()