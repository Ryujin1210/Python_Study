# def calculate_area(length, width=10):
#     return length * width
# print(calculate_area(5))
# print(calculate_area(5, 20))

# def add_numbers(a, b=0):
#     return a + b
# print(add_numbers(10))

# def inner_function(x, y):
#         return x + y
# def outer_function(x, y):
#     return inner_function(x, y)
# add_10 = outer_function(10, 5)
# print(add_10)

# result = 0
# def add_numbers(a, b):
#     result = a + b
# print(result)

# def message() :
#     print("A")
#     print("B")
# message()
# print("C")
# message()


# print("A")
# def message() :
#     print("B")
# print("C")
# message()

# def check_odd_even(n):
#     if n % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# print(check_odd_even(4))
# print(check_odd_even(7))

# def calculate_average(num_list):
#     return sum(num_list) / len(num_list)


# num_list = [10, 20, 30, 40, 50]
# average = calculate_average(num_list)

# print("평균: ", average)


# from dataclasses import dataclass

# @dataclass
# class SensorLog:
#     temp: float        # 타입 있음
#     unit = "℃"         # 타입 없음

# print(SensorLog(78.2))

# log = SensorLog(78.2)

# print(log.unit)

from dataclasses import dataclass

@dataclass
class Bad:
    temp: float
    status: str = "OK"

# @dataclass
# class Bad:
#     history: list = [] # 이렇게 사용하면 안됌, 하나의 리스트에 계속 작업하는걸로 함


from dataclasses import dataclass, field

@dataclass
class Good:
    history: list[float] = field(default_factory=list)   # 객체마다 새 리스트