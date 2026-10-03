import os

f = open(r"./file1.txt", "r", encoding="utf-8")

lines = f.readlines()

# for line in lines:
#     print(line, end="")

print(lines)