# try:
#     x = int("abc")
# except ValueError:
#     print("ValueError occurred!")
# finally:
#     print("Execution finished.")

# try: 
#     x = 10 / 0
# except ZeroDivisionError:
#     print("Cannot divide by zero!")

# raise KeyError("Key is missing!")

# add = lambda x, y: x + y 
# x, y = map(int, input().split())
# print(add(x, y))

# per = ["10.31", "", "8.00"]

# for i in per:
#     try:
#         print(float(i))
#     except ValueError:
#         i = 0 
#         print(i)

numbers = [10, 20, 30]

def index_check():
    try:
       i = int(input("인덱스 입력: "))
       print(numbers[i]) 
    except IndexError:
       print("잘못된 인덱스 입니다.")
    except ValueError:
       print("숫자를 입력해야합니다!")
       
index_check()