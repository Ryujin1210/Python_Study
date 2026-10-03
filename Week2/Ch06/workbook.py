# def example(a, b=3):
#     return a + b
# print(example(5))

# def print_hello():
#     print("안녕하세요")

# for i in range(100):
#     print_hello()   

# def greet(name):
#     print(f"Hello, {name}!")

# greet("Alice")


# num1 = int(input("첫 번째 숫자를 입력하세요: "))
# num2 = int(input("두 번째 숫자를 입력하세요: "))

# print("덧셈:", num1 + num2)
# print("뺄셈:", num1 - num2)
# print("곱셈:", num1 * num2)
# print("나눗셈:", num1 / num2)

# score = int(input("점수를 입력하세요: "))

# if score >= 90:
#     print("A학점")
# elif score >= 80:
#     print("B학점")
# elif score >= 70:
#     print("C학점")
# else:
#     print("F학점")

# fruits = ["banana", "peach", "lemon", "grape"]
# print(fruits[2])

# students = {"나이": 22, "직업": "학생", "취미": "게임"}
# students["도시"] = "수원"
# students.update({"국가" : "대한민국"})

# print(students)

# Numbers = [1,2,3,4,5]
# for num in Numbers:
#     print(num)

# fruits = ['바나나', '파인애플', '복숭아', '사과', '포도']
# for apple in fruits: 
#     print(apple)

#     if apple == '사과':
#         print('사과를 찾았습니다!')

# def solution(a, b):
#     sum = a + b
#     sub = a - b
#     multi = a * b
#     return sum, sub, multi

# a, b = map(int, input("두 수를 입력하세요: ").split())

# sum, sub, multi = solution(a, b)

# print("합:", sum)
# print("차:", sub)
# print("곱:", multi)

def mulsum(end):
    total = 0
    for i in range(end + 1):
        total += i
    return total

print(mulsum(100))
    