import os 

pizza = {
    "페퍼로니피자" : 3000,
    "치즈피자" : 3200,
    "콤비네이션피자" :3500
}
pizza_apd = {
    "불고기피자" : 3600,
    "해산물피자" : 3800
}

all_pizza_name = []

with open("./pizza_file.txt", "w", encoding= "utf-8") as f:
    for name, price in pizza.items():
        f.write(f"{name} {price}\n")

with open("./pizza_file.txt", "a", encoding= "utf-8") as f:
    for name, price in pizza_apd.items():
        f.write(f"{name} {price}\n")

with open("./pizza_file.txt", "r", encoding= "utf-8") as f:
    for line in f:
        name, _ = line.strip().split()
        all_pizza_name.append(name)

print(all_pizza_name)

# with open("./pizza_file.txt", "w", encoding= "utf-8") as f:
#     f.write("페퍼로니피자\n치즈피자\n콤비네이션피자")