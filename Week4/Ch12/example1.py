import os

# with open ("./계좌1.txt", "w") as f:
#     f.write("김삿갓 597-89-00008\n이수근 343-64-000064\n박혁거세 136-97-000097") 
    

accounts = [
    "김삿갓 597-89-00008",
    "이수근 343-64-000064",
    "박혁거세 136-97-000097"
]

with open("./계좌1.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(accounts))
    
# with open("./계좌1.txt", "w", encoding="utf-8") as f:
#     for account in accounts:
#         f.write(account + "\n")