# arr = [3, 6, 9, 12]
# arr[0], arr[2] = arr[2], arr[0]
# print(arr)

# a = [1, 2, 3]
# b = a
# print(id(a) == id(b))

# x = 42
# y = 42
# print(id(x) == id(y))

# a = [3, 6, 7, 4, 9, 10, 13]
# odd = 0
# even = 0 

# for i in range(len(a)):
#     if a[i] % 2 == 0:
#         even = i
#         break

# for i in range(len(a)-1, -1, -1):
#     if a[i] % 2 == 1:
#         odd = i
#         break
# a[even], a[odd] = a[odd], a[even]
# print(a)
    
# a = [3, 6, 7, 4, 9, 10, 13]
# max = 0
# for i in a:
#     if max < i:
#         max = i
# print(max)

# dict = { 'a': 10, 'b': 20, 'c': 30 }
# def dict_sum(a):
#     result = 0
#     for i in a:
#         result += a[i]
#     return result
# print(dict_sum(dict))

numbers = [42, 17, 23, 56, 9, 34]

def list_min(num_list):
    min = num_list[0]
    for num in num_list:
        if min > num:
            min = num
    print(min)
 
list_min(numbers)