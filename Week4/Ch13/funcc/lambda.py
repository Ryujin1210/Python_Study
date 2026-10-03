# 일반적 함수 정의 및 호출
def square1(x):
    return x * x

# lambda 인자 : 표현식
# lambda 매개변수 : 표현식
square = lambda x : x ** 2

print(square1(3))
print(square(3))
print((lambda x : x ** 2)(3))

##################################
# 표현식 (Expression)
# : 실행됐을때 하나의 값을 만들어내는 코드
# 1. 값
# 10 + 20
# x * 2
# a > b
# 2. 변수
# X = 10
# print(x)
# 3. 함수 호출 
# len("Python")
# 4. 조건 표현식
# age = 20
# result = "성인" if age >= 18 else "미성년자"
