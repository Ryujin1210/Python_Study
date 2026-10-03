import os

f = open(r"./file1.txt", "w", encoding="utf-8" )

for i in range(1, 11):
    # data = "%d번째 줄입니다.\n" % i # 이전 포매팅 방법 
    data = f"{i}번째 줄입니다.\n"
    f.write(data)

f.close()