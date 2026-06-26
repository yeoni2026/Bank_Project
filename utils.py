#utils.py
def get_safe_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("숫자만 입력할 수 있습니다. 다시 입력해 주세요.")