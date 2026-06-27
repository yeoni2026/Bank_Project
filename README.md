# BANK PROJECT 설명 (파일별)

## main.py
- 핵심 흐름 담당

## account.py
- 하나의 계좌 내에서 상태, 변화 등 관리
- 예금(`deposit()`), 출금(`withdraw()`), 계좌정보 확인(`info()`) 등의 함수 존재

## account_manager.py
- 전체 계좌 리스트 관리
- 계좌를 찾거나(`find_account`), 계좌를 만드는(`open_account`) 함수 포함
- 계좌 리스트 저장과 불러오기 <=> bank_data.json

## handler.py
- 사용자와 입출력 상호작용하는 함수들.
- main.py와 다른 파일들(account.py 등)을 연결시키는 중간다리 역할.

## utils.py
- 코딩에 도움 주는 기능들 (예외처리 등)

## test_account.py
- account.py 관련 테스트 (pytest)

## bank_data.json
- 계좌 데이터 저장