#main.py
from utils import get_safe_int
from account_manager import AccountManager
from handler import handle_deposit, handle_withdraw, handle_find_account


manager = AccountManager()

while True:
    menu1 = get_safe_int("1. 계좌개설 2. 계좌조회 : ")

    if menu1 == 1:
        manager.open_account()
    elif menu1 == 2:
        acc = handle_find_account(manager)
        if acc == None:
            continue

        while True:
            menu2 = get_safe_int("1. 입금 2. 출금 3. 계좌상태 4. 계좌내역 5. 종료 : ")
            if menu2 not in [1, 2, 3, 4, 5]:
                print("1부터 5사이의 숫자만 입력해 주세요.")
                continue 
            if menu2 == 5:
                break
            match menu2:
                case 1:
                    handle_deposit(acc)
                case 2:
                    handle_withdraw(acc)
                case 3:
                    acc.info()
                case 4:
                    acc.show_history()
    else : 
        print("1부터 2사이의 숫자만 입력해주세요.")
        continue

    manager.save_data()
    print("이용해 주셔서 감사합니다.")
    break