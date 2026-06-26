from utils import get_safe_int
from datetime import datetime


class Account:
    
    def __init__(self, number : str, name : str, remains : int = 0, history = None):
        self.number = number
        self.name = name
        self.remains = remains
        self.history = history if history is not None else []

    def deposit(self, money):
        if money <= 0:
            raise ValueError("0원 이하의 금액은 입금할 수 없습니다.")
        
        self.remains += money
        self.add_history("입금", money)
    
    def withdraw(self, money):     
        if money <= 0:
            raise ValueError("0원 이하의 금액은 출금할 수 없습니다.")
        if self.remains < money:
            raise ValueError("잔액이 부족하여 출금할 수 없습니다.")
        
        self.remains -= money
        self.add_history("출금", money)
        
    def add_history(self, type, amount):
        now = datetime.now()
        string_time = now.strftime("%Y-%m-%d %H:%M:%S")
        record_dic = {"date" : string_time, "type" : type, "amount" : amount, "balance_after" : self.remains}
        self.history.append(record_dic)

    def show_history(self):
        recent_history = self.history[-5:]

        if not recent_history:
            print("거래 내역이 없습니다.")
            return

        max_digit_amount = max(len(str(item.get("amount", 0))) for item in recent_history)
        max_digit_balance = max(len(str(item.get("balance_after", 0))) for item in recent_history)

        for item in recent_history:
            print(f'{item.get("date")} | {item.get("amount"):{max_digit_amount}d}원 {item.get("type")} | 잔액: {item.get("balance_after"):{max_digit_balance}d}원')
        print("최근 내역 최대 5개까지 보여줍니다.")

    def info(self):
        print(f"계좌번호: {self.number} | 이름: {self.name} | 잔액: {self.remains}원")