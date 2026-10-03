import os

f = open(r"./file1.txt", "a", encoding="utf-8")

for i in range(11,20):
    data = f"{i}번째 줄입니다.\n"
    f.write(data)
f.close()