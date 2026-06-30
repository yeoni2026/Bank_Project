#handler.py
from utils import get_safe_int

def handle_deposit(acc):
    while True:
        money = get_safe_int("얼마를 입금하실 건가요? : ")
        try:
            acc.deposit(money)  
            print("입금 완료되었습니다!")
            break
        except ValueError as e: 
            print(e)

def handle_withdraw(acc):
    while True:
        money = get_safe_int("얼마를 출금하실 건가요? : ")
        try:
            acc.withdraw(money)  
            print("출금 완료되었습니다!")
            break
        except ValueError as e: 
            print(e)

def handle_find_account(manager):
    while True:
        account_number = input(f"조회할 계좌의 계좌번호를 입력하세요 : ")
        acc = manager.find_account(account_number)
        if acc:
            try_count = 0
            while True:
                try_count += 1
                pin = input("계좌 비밀번호를 입력하세요 : ")
                if acc.verify_pin(pin):
                    return acc
                else :
                    if try_count >= 3:
                        print("비밀번호 입력에 3번 실패하여 메인 메뉴로 돌아갑니다.")
                        return None
                    else : 
                        print("비밀번호가 일치하지 않습니다.")
                    
        else : 
            print("존재하지 않는 계좌번호입니다.")
            return None

