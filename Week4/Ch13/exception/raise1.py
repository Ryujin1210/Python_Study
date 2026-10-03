# raise 예외클래스명(예외 정보 데이터)

print("raise1")
try:
    raise NameError("Hi There")
except NameError as e:
    print("Anncecs", e)
print("exit")

# 주요 사용 이유
# - 잘못된 값 입력 방지 
# - 함수에서 조건을 위반 시 중단
# - 사용자 정의 에러 처리 

# Ex. 은행 잔고 부족시 예외 발생

# 사용자 정의 에러 클래스 - 상속 받아서 사용자 에러 만듦
class errorBalanceError(Exception):
    pass

class Account:
    def __init__(self, balance):
        self.balance = balance
        
    def withdraw(self, ammount):
        if ammount > self.balance:
            raise errorBalanceError("잔고 부족")
        self.balance -= ammount
        return self.balance
    
Ryu = Account(1000)

try:
    print(Ryu.withdraw(1500))
except errorBalanceError as e:
    print("출금 실패:". e)