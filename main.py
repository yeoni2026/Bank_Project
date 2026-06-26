from utils import get_safe_int
from account_manager import AccountManager
from handler import handle_deposit, handle_withdraw, handle_find_account


menu_names = {2: "입금", 3: "출금", 4: "확인", 5: "확인"}
manager = AccountManager()

while True:
    menu = get_safe_int("1. 계좌개설 2. 입금 3. 출금 4. 계좌상태 5. 계좌내역 6. 종료 : ")
    if menu not in [1, 2, 3, 4, 5, 6]:
        print("1부터 5사이의 숫자만 입력해 주세요.")   
        continue 
    if menu == 1:
        manager.open_account()
        continue
    if menu == 6:
        print("이용해 주셔서 감사합니다.")
        manager.save_data()
        break
    msg = menu_names.get(menu)
    acc = handle_find_account(manager, msg)
    match menu:
        case 2:
            handle_deposit(acc)
        case 3:
            handle_withdraw(acc)
        case 4:
            acc.info()
        case 5:
            acc.show_history()