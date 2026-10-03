b = 0
print("b값: ", b)
b = 1
print("b값: ", b)

def scope_test():
    global a
    a = 1
    print("함수 내 a의 값: ", a)
    
a = 0 
print("함수 밖 a의 값: ", a)
scope_test()
print("함수 호출 후 a의 값: ", a)