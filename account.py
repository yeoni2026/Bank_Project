class Account:
    def __init__(self, number : str, name : str, remains : int = 0):
        self.number = number
        self.name = name
        self.remains = remains
    def deposit(self, money):
        self.remains += money
    def withdraw(self, money):
        if self.remains >= money:
            self.remains -= money
            return True
        else :
            return False
    def info(self):
        print(f"계좌번호: {self.number} | 이름: {self.name} | 잔액: {self.remains}")