import random
from account import Account

account_list = []
menu_names = {2: "입금", 3: "출금", 4: "확인"}
while True:
    menu = int(input("1. 계좌개설 2. 입금 3. 출금 4. 계좌확인 5. 종료 : "))
    if menu == 1:
        guest = input("이름을 입력해주세요 : ")
        random_num = random.randint(0,9999)
        account_number = f"{random_num:04d}"
        print(f"계좌가 개설되었습니다! 계좌번호는 {account_number}입니다.")
        acc = Account(account_number, guest)
        account_list.append(acc)
    elif menu == 5:
        print("이용해 주셔서 감사합니다.")
        break
    else:
        msg = menu_names.get(menu)
        while True:
            account_number = input(f"{msg}할 계좌의 계좌번호를 입력하세요 : ")
            for acc in account_list:
                if acc.number == account_number:
                    break
            else : 
                print("존재하지 않는 계좌번호입니다.")
                continue
            break
        match menu:
            case 2:
                money = int(input("얼마를 입금하실 건가요? : "))
                acc.deposit(money)
                print("입금 완료되었습니다!")
            case 3:
                money = int(input("얼마를 출금하실 건가요? : "))
                if acc.withdraw(money):
                    print("출금 완료되었습니다!")
                else: print("잔액이 부족하여 출금 실패하였습니다.")
            case 4:
                acc.info()