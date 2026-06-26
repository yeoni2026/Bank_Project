import random
from account import Account
import json
import sys


class AccountManager():

    def __init__(self):
        self.account_list = []
        self.load_data()

    def find_account(self, account_number):
        for acc in self.account_list:
            if acc.number == account_number:
                return acc
        else : 
            return None

    def open_account(self): 
        
        guest = input("이름을 입력해주세요 : ")
        if any(guest == acc.name for acc in self.account_list):
            print(f"{guest}님의 계좌는 이미 존재합니다. 한 사람당 하나의 계좌만 사용가능합니다.")
            return
        
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
        data = [{"number" : acc.number, "name" : acc.name, "remains" : acc.remains, "history" : acc.history} for acc in self.account_list]
        with open("bank_data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def load_data(self):
        try:
            with open("bank_data.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                for item in data:
                    acc = Account(item.get("number"), item.get("name"), item.get("remains"), item.get("history"))
                    self.account_list.append(acc)
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"데이터 파일이 손상되었거나 형식 오류가 발생하여 종료합니다. (원인: {e})")
            sys.exit()