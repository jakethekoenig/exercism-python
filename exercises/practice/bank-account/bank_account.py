class BankAccount:
    def __init__(self):
        self.is_open = False
        self.balance = 0

    def get_balance(self):
        if not self.is_open:
            raise ValueError('account not open')
        return self.balance

    def open(self):
        if self.is_open:
            raise ValueError('account already open')
        self.is_open = True

    def deposit(self, amount):
        if not self.is_open:
            raise ValueError('account not open')
        if amount <= 0:
            raise ValueError('amount must be greater than 0')
        self.balance += amount

    def withdraw(self, amount):
        if not self.is_open:
            raise ValueError('account not open')
        if amount <= 0:
            raise ValueError('amount must be greater than 0')
        if amount > self.balance:
            raise ValueError('amount must be less than balance')
        self.balance -= amount

    def close(self):
        if not self.is_open:
            raise ValueError('account not open')
        self.is_open = False
        self.balance = 0
