import os 

accounts = []

with open("./계좌1.txt", "r") as f:
    # for line in f.readlines():
    #     accounts.append(line[-13:])
    
    # for line in f:
        # name, account = line.strip().split()
        # accounts.append(account)
        
    for line in f:
        line = line.strip()
        accounts.append(line[line.rfind(" ") + 1:])

print(accounts)

