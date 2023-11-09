from threading import Lock

class BankAccount:
    def __init__(self):
        self._balance = 0
        self._is_open = False
        self._lock = Lock()

    def get_balance(self):
        if not self._is_open:
            raise ValueError('account not open')
        with self._lock:
            return self._balance

    def open(self):
        if self._is_open:
            raise ValueError('account already open')
        self._is_open = True
        self._balance = 0

    def deposit(self, amount):
        if not self._is_open:
            raise ValueError('account not open')
        if amount <= 0:
            raise ValueError('amount must be greater than 0')
        with self._lock:
            self._balance += amount

    def withdraw(self, amount):
        if not self._is_open:
            raise ValueError('account not open')
        if amount <= 0:
            raise ValueError('amount must be greater than 0')
        with self._lock:
            if amount > self._balance:
                raise ValueError('amount must be less than balance')
            self._balance -= amount

    def close(self):
        if not self._is_open:
            raise ValueError('account not open')
        self._is_open = False
        self._balance = 0
