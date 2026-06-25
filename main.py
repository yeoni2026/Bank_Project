from utils import get_safe_int
from account_manager import AccountManager

menu_names = {1: "개설", 2: "입금", 3: "출금", 4: "확인", 5: "종료"}
manager = AccountManager()

while True:
    menu = get_safe_int("1. 계좌개설 2. 입금 3. 출금 4. 계좌확인 5. 종료 : ")
    if menu not in [1, 2, 3, 4, 5]:
        print("1부터 5사이의 숫자만 입력해 주세요.")   
        continue 
    if menu == 1:
        manager.open_account()
        continue
    if menu == 5:
        print("이용해 주셔서 감사합니다.")
        manager.save_data()
        break
    msg = menu_names.get(menu)
    acc = manager.find_account(msg)
    match menu:
        case 2:
            acc.deposit()
        case 3:
            acc.withdraw()
        case 4:
            acc.info()