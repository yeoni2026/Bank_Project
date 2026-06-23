import random
from account import Account
from utils import get_safe_int

account_list = []
menu_names = {2: "입금", 3: "출금", 4: "확인"}

def find_account(account_list, msg):
    while True:
        account_number = input(f"{msg}할 계좌의 계좌번호를 입력하세요 : ")
        for acc in account_list:
            if acc.number == account_number:
                return acc
        else : 
            print("존재하지 않는 계좌번호입니다.")

def open_account(account_list):
    guest = input("이름을 입력해주세요 : ")
    while True:
        random_num = random.randint(0,9999)
        account_number = f"{random_num:04d}"
        if any(acc.number == account_number for acc in account_list):
            continue
        print(f"계좌가 개설되었습니다! 계좌번호는 {account_number}입니다.")
        acc = Account(account_number, guest)
        account_list.append(acc)
        break

while True:
    menu = get_safe_int("1. 계좌개설 2. 입금 3. 출금 4. 계좌확인 5. 종료 : ")
    if menu not in [1, 2, 3, 4, 5]:
        print("1부터 5사이의 숫자만 입력해 주세요.")   
        continue 
    if menu == 1:
        open_account(account_list)
        continue
    if menu == 5:
        print("이용해 주셔서 감사합니다.")
        break
    msg = menu_names.get(menu)
    acc = find_account(account_list, msg)
    match menu:
        case 2:
            acc.deposit()
        case 3:
            acc.withdraw()
        case 4:
            acc.info()