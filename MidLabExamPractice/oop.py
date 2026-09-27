class BankAccount:
    """Base class demonstrating encapsulation and dunder methods."""

    def __init__(self, owner, initial_balance):
        self.owner = owner
        # Encapsulation: The double underscore triggers name mangling
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        """Controlled access to the private attribute."""
        return self.__balance

    def __str__(self):
        return f"BankAccount(Owner: {self.owner})"


class SavingsAccount(BankAccount):
    """Subclass demonstrating inheritance and method overriding."""

    def __init__(self, owner, initial_balance, interest_rate):
        # super() safely calls the parent's __init__
        super().__init__(owner, initial_balance)
        self.interest_rate = interest_rate

    def __str__(self):
        # Overriding __str__ while still leveraging the parent's logic
        parent_str = super().__str__()
        return f"{parent_str} | Savings Rate: {self.interest_rate}%"


# Execution
my_account = SavingsAccount("Alice", 1000, 4.5)
print(my_account)
# Output: BankAccount(Owner: Alice) | Savings Rate: 4.5%

print(f"Current Balance: ${my_account.get_balance()}")
# Output: Current Balance: $1000