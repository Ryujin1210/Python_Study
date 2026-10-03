import os 

accounts = {}

with open("./계좌1.txt", "r") as f:
    
    for line in f:
        name, account = line.strip().split()
        accounts[name] = account

print(accounts)

accounts = {}

# with open("./계좌1.txt", "r", encoding="utf-8") as f:
#     lines = f.readlines()

# for line in lines:
#     name, account = line.strip().split()
#     accounts[name] = account

