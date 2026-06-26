from account import Account

def test_deposit():
    acc = Account("0001", "철수")
    acc.deposit(10000)
    assert acc.remains == 10000

def test_withdraw():
    acc = Account("0001", "영희")
    try:
        acc.withdraw(-10000)
        assert False
    except:
        pass