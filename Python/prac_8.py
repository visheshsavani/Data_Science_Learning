class Account:
    def __init__(self,acc_no,balance) -> None:
        self.acc = acc_no
        self.bal = balance
    def debit(self,x):
        self.bal = self.bal-x
    def credit(self,y):
        self.bal = self.bal+y
    def show_balance(self):
        return self.bal

a1 = Account(5748393,1000)
a1.credit(50)
print(a1.show_balance())
a1.debit(20)
print(a1.show_balance())
