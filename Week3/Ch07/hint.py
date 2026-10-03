# def add(x: int, y: int) -> int :
#     return x + y

# print(add(3.2, 5))
# print(add("문자열", 5))

# def count_down(n):
#     if n == 0:
#         print("완료!")
#         return
#     print(n)
#     count_down(n-1)

# count_down(4)

# def factorial(n):
#     if n == 0:
#         return 1

#     return n * factorial(n - 1)

# print(factorial(3))

# x = 10
# def fadd(num):
#     global x
#     x=x+num
#     print(x)
     
# fadd(10)     
price = int(input())
def print_lower_price(p):
    p *= 0.9
    return p
        
print(print_lower_price(price))
    