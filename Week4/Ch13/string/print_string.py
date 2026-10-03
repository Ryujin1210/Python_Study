# 문자열 출력 방식

name = "홍길동"
age = 700
height = 191.3

# 기본 형식
# 1. print("내용1", "내용2")

print("이름:", name, "나이:", age, "신장:", height)

# 2. % 연산자 사용 방식
# 서식문자 활용 -> %s: 문자열, %d: 십진수,정수, %f: 실수 

print("이름: %s, 나이: %d, 신장: %.1f" %(name, age, height))

# 3. format() 메서드 사용 방식 
print("이름: {}, 나이: {}, 신장: {}".format(name, age, height))

# 4. f-string 사용 방식
print(f"이름: {name}, 나이: {age}, 신장: {height: .3f}")