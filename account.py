from utils import get_safe_int
from datetime import datetime

class Account:
    def __init__(self, number : str, name : str, remains : int = 0, history = None):
        self.number = number
        self.name = name
        self.remains = remains
        self.history = history if history is not None else []

    def deposit(self):
        while True:
            money = get_safe_int("얼마를 입금하실 건가요? : ")
            if money <= 0:
                print("0원 이하의 금액은 입금할 수 없습니다.")
                continue
            self.remains += money
            print("입금 완료되었습니다!")
            self.add_history("입금", money)
            return True
        
    def withdraw(self):
        while True:
            money = get_safe_int("얼마를 출금하실 건가요? : ")
            if money <= 0:
                print("0원 이하의 금액은 출금할 수 없습니다.")
                continue
            if self.remains < money:
                print("잔액이 부족하여 출금할 수 없습니다.")
                continue
            self.remains -= money
            print("출금 완료되었습니다!")
            self.add_history("출금", money)
            return True
        
    def add_history(self, type, amount):
        now = datetime.now()
        string_time = now.strftime("%Y-%m-%d %H:%M:%S")
        record_dic = {"date" : string_time, "type" : type, "amount" : amount, "balance_after" : self.remains}
        self.history.append(record_dic)

    def info(self):
        print(f"계좌번호: {self.number} | 이름: {self.name} | 잔액: {self.remains}원")