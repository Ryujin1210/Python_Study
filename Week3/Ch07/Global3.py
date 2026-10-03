def scope_test(na):
    na += 3 # a가 선언 되기전에 산술하여 오류 발생 : 산술 > 대입 
    print("함수 내 a의 값: ", a)
    
a = 0 
print("함수 밖 a의 값: ", a)
scope_test(a)
print("함수 호출 후 a의 값: ", a)

def scope_test2():
    global b
    b += 3 
    print("함수 내 b의 값: ", a)
    
b = 0 
print("함수 밖 b의 값: ", b)
scope_test2()
print("함수 호출 후 b의 값: ", b)

