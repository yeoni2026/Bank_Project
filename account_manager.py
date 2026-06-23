import random
from account import Account
import json

class Account_manager():

    def __init__(self):
        self.account_list = []
        self.load_data()

    def find_account(self, msg):
        while True:
            account_number = input(f"{msg}할 계좌의 계좌번호를 입력하세요 : ")
            for acc in self.account_list:
                if acc.number == account_number:
                    return acc
            else : 
                print("존재하지 않는 계좌번호입니다.")

    def open_account(self):
        guest = input("이름을 입력해주세요 : ")
        while True:
            random_num = random.randint(0,9999)
            account_number = f"{random_num:04d}"
            if any(acc.number == account_number for acc in self.account_list):
                continue
            print(f"계좌가 개설되었습니다! 계좌번호는 {account_number}입니다.")
            acc = Account(account_number, guest)
            self.account_list.append(acc)
            break

    def save_data(self):
        data = [[acc.number, acc.name, acc.remains] for acc in self.account_list]
        with open("bank_data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def load_data(self):
        try:
            with open("bank_data.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                for item in data:
                    acc = Account(item[0], item[1], item[2])
                    self.account_list.append(acc)
        except FileNotFoundError:
            pass