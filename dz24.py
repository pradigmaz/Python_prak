# первый вариант

class Account:
    def __init__(self, balance=0):
        self._balance = balance  # внутреннее поле

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value  # без проверок, максимально просто

# пример использования
a = Account()
a.balance = 1000
print(a.balance)  # 1000

# 2 вариант

class Account2:
    def __init__(self, balance=0):
        self._balance = balance  # внутреннее поле

    def get_balance(self):
        return self._balance

    def set_balance(self, value):
        self._balance = value  # без проверок, максимально просто

# пример использования
a2 = Account2()
a2.set_balance(1000)
print(a2.get_balance())  # 1000
