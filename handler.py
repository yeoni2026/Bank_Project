from utils import get_safe_int

def handle_deposit(acc):
    while True:
        money = get_safe_int("얼마를 입금하실 건가요? : ")
        try:
            acc.deposit(money)  
            print("입금 완료되었습니다!")
        except ValueError: 
            continue

def handle_withdraw(acc):
    while True:
        money = get_safe_int("얼마를 출금하실 건가요? : ")
        try:
            acc.withdraw(money)  
            print("출금 완료되었습니다!")
        except ValueError: 
            continue

def handle_find_account(manager, msg):
    while True:
        account_number = input(f"{msg}할 계좌의 계좌번호를 입력하세요 : ")
        acc = manager.find_account(account_number)
        if acc:
           return acc
        else : print("존재하지 않는 계좌번호입니다.")

