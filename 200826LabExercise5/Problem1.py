class BankAccount:
    def __init__(self, account_no, holder_name, balance):
        self.account_no = account_no
        self.holder_name = holder_name
        self.__balance = balance

    def deposit(self, amount):
        self.__balance+=amount

    def withdraw(self, amount):
        if(amount>self.__balance):
            raise Exception("Insufficient balance")
        self.__balance -= amount

    def get_balance(self):

        print("Current Balance: ",self.__balance)
    def __str__(self):
        return "Account No.: "+str(self.account_no)+"\nHolder Name: "+self.holder_name +"\nBalance: "+str(self.__balance)
try:
    account1 = BankAccount(101,"Sathish", 5000)
    account2 = BankAccount(102,"Rakesh", 3000)
    print(account1)
    account1.deposit(1000)
    account1.get_balance()

    account1.withdraw(2000)
    account1.get_balance()
    print()
    print(account2)
    account2.deposit(500)
    account2.get_balance()
    account2.withdraw(1000)
    account2.get_balance()
except Exception as e:
    print("error: ", e)
    