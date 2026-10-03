# import math

# print(math.factorial(5))

# from math import factorial
# print(factorial(5))

# class Animal:
#     def speak(self):
#         return "Animal speaks"
    
# class Dog(Animal):
#     def speak(self):
#         return "Woof!"

# milk = Dog()
# print(milk.speak())

# with open("./data.txt", "w", encoding = "utf-8") as file:
#     for i in range(1, 11):
#         file.write(f"{i}번째 줄입니다.\n")

# print("파일이 성공적으로 작성되었습니다.")

# with open("./data.txt", "a", encoding="utf-8") as file:
#     file.write("11번째 줄입니다.")

# with open("./data.txt", "r", encoding="utf-8") as file:
#     contents = file.read()

# print("파일 내용:")
# print(contents)

# while True:
#     try:
#         a = int(input("숫자를 입력해주세요."))
#         print((lambda x : x ** 2)(a))
#         break
#     except ValueError:
#         print("올바른 숫자를 입력하세요!\n")
    
num_list = [10, 20, 30, 40, 50]
print(list(map(lambda x : x ** 2, num_list)))