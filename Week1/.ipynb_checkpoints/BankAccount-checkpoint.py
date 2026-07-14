class BankAccount:

    def __init__(self,Owner_name,Account_number,Balance):
        self.Owner_name=Owner_name
        self.Account_number=Account_number
        self.Balance=Balance

    def deposit(self,amount):
        if amount>0:
             self.Balance+=amount
             print("deposited succesfully")
    
    def withdraw(self,amount):
        if self.Balance > amount:
            self.Balance-=amount
            print("withdraw successfully")
        else:
            print("Balance insufficient")

    def check_balance(self):
        print(f"Account holder:{self.Owner_name} has balance {self.Balance}")

User1 = BankAccount("riya",123,100000)
User1.check_balance()

User1.deposit(50000)
User1.check_balance()

User1.withdraw(25000)
User1.check_balance()



          