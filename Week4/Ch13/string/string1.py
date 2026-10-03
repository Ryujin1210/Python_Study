muna = "python"
print(muna[0])
print(muna[1])
print(muna[2])
print(type(muna))

# muna[0] = 'k'  # 문자열은 이뮤터블 

try:
    muna[0] = 'k'
except TypeError as e:
    print(type(e), e)
    
###################
munb = ["python"]
print(munb[0])
print(type(munb[0]))

######################
munc = list(muna)
print(munc[0])
print(munc[1])
print(munc[2])

munc[0] = 'k'
print(munc)

###########
for i in range(0,len(munc),1):
    print(munc[i], end="")
print()

print(len(munc))

##########
print(ord("A"))
print(ord("a"))
print(chr(65))
print(chr(97))

###############
import locale
print(locale.getpreferredencoding())

###############

ma = "chagpt" + "를 활용한 python"
print(ma)