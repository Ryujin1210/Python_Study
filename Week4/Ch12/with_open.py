import os

path = "./file2.txt"
mode = "w"

with open(path, mode) as f:
    num = f.write("no pain no gain!")
    print(num)