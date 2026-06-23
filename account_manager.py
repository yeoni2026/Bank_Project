import random
from account import Account

class Account_manager():

    def __init__(self):
        self.account_list = []

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
