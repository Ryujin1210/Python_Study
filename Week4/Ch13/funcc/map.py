# map (함수, 이터레이터)

def square(x):
    return x ** 2

print(square(2))

################

square2 = lambda x:x ** 2
print(square2(2))

################
num = [1,2,3,4,5,6]
squred_num = map(square, num)
print(list(squred_num))

#################
num2 = [1,2,3,4,5,6]
squared_num2 = map(lambda x: x ** 2, num2)
print(list(squared_num2))
