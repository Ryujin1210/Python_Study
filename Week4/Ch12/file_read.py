import os

f = open(r"./file1.txt", "r", encoding="utf-8")

data = f.read()

# print(data)

# 줄바꿈 문자를 표시 함수
print(repr(data))

f.close()