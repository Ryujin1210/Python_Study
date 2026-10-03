# for a in [10, 20, 30]:
#     print(a)
    
# for a in [100, 200, 300]:
#     print(a+10)
   
# animals = ['dog', 'cat', 'parrot']
# for animal in animals:
#     print(animal, len(animal))

# ch = ['가', '나', '다', '라']
# for c in range(1, len(ch)):
#     print(ch[c])
    
# for c in ch[1: ]:
#     print(c)

# r = [3, -20, -3, 44]
# for m in r:
#     if m < 0:
#         print(m)

# for ol in range(2002, 2051, 4):
#     print(ol)
# i = 1
# total = 0
# while i <= 100:
#     total += i
#     i += 1
# print(total)

# for i in range(1,3):
#     for j in range(1, 10):
#         print(i * j)

even = []
odd = []

for i in range(1,31):
    if i % 2 == 0:
        print(i, ": 짝수")
        even.append(i)
    else:
        print(i, ": 홀수")
        odd.append(i)
print(even)
print(odd)