# def funca(cb):
#     temp = cb[0]
#     cb[0] = cb[1]
#     cb[1] = temp 
    
# ca=[10 ,11]

# print(ca)
# funca(ca)
# print(ca)

# def funca(cb):
#     cb = [100, 200]

# ca = [10, 11]

# funca(ca)
# print(ca)

# ========================================
# a = [10, 11, 12, 13]
# print(a)
# b = a 
# print(b)

# ========================================

def fk(cb):
    total=0
    for sb in range (0, 3, 1):
        total+= cb[sb]
    cb[2] = total
    return cb
ca=[10,20,30]
print(ca) # 10, 20, 30
cd=fk(ca) # 10, 20, 60
print(ca) # 10, 20, 60
print(cd) # 10, 20, 60