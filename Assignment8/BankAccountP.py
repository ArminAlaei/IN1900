# 8.4. Extending the BankAccountP class

class BankAccountP:
    def __init__(self, first_name, last_name, number, balance):
        self._first_name = first_name
        self._last_name = last_name
        self._number = number
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    def get_balance(self):    # NEW - read balance value
        return self._balance

    def print_info(self):
        first = self._first_name; last = self._last_name
        number = self._number; bal = self._balance
        s = f'{first} {last}, {number}, balance: {bal}'
        print(s)
    def Transfer(self, amount,account2):
        self.withdraw(amount)
        account2.deposit(amount)

a1 = BankAccountP('John', 'Olsson', '19371554951', 20000)
a2 = BankAccountP('Liz', 'Olsson',  '19371564761', 20000)

a1.deposit(1000)
a1.withdraw(4000)
a2.withdraw(10500)
a1.withdraw(3500)
print("a1's balance:", a1.get_balance())
a1.print_info()
a2.Transfer(500,a1)
print(a2.get_balance())

def test_BankAccountP():
    #Creating instances for testing the class
    a4 = BankAccountP('Armin', 'Alaei', '19341564981', 0)
    a6 = BankAccountP('Arne', 'Nordmann', '19341164921', 5000)

    #The expected values
    expected_dep = 5000
    expected_with = 4500
    expected_trns = 2500
    expected_bal = 2500

    #Testing the methods
    a4.deposit(5000)
    success_dep = a4.get_balance() == expected_dep
    msg_dep = "failed to deposit amount"
    assert success_dep,msg_dep

    a4.withdraw(500)
    success_with = a4.get_balance() == expected_with
    msg_with = "failed to withdraw amount"
    assert success_with,msg_with

    a4.Transfer(2000,a6)
    success_trns = a4.get_balance()== expected_trns
    msg_trns = "failed to transfer correct amount"
    assert success_trns, msg_trns

    success_bal = a4.get_balance()== expected_bal
    msg_bal = "failed to get correct balance"
    assert success_bal, msg_bal







test_BankAccountP()

"""

(When testing the test function in pycharm the test function passes)

Run example:

user$ python3 BankAccountP.py


output:

a1's balance: 13500
John Olsson, 19371554951, balance: 13500

"""
