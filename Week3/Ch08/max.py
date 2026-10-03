# ca = [10, 17, 13, 11]
# max = ca[0]
# # if max < ca[1]:
# #     max = ca[1]
# # if max < ca[2]:
# #     max = ca[2]
# # if max < ca[3]:
# #     max = ca[3]
# # print(max)
# for sb in range(1, 4, 1):
#     if max < ca[sb]:
#         max = ca[sb]
# print(max)

# ca = [21, 10, 11, 15, 13]
# mina = ca[0]
# minx = 0

# for sb in range(1, 5, 1):
#     if mina > ca[sb]:
#         mina = ca[sb]
#         minx = sb
# temp = ca[0]
# ca[0] = ca[minx]
# ca[minx] = temp
# print(ca)

# mina = ca[1]
# minx = 1

# for sb in range(2, 5, 1):
#     if mina > ca[sb]:
#         mina = ca[sb]
#         minx = sb
# temp = ca [1]
# ca[1] = ca[minx]
# ca[minx] = temp
# print(ca)

ca = [21, 10, 11, 15, 13]

for sa in range(0, 4):
    mina = ca[sa]
    minx = sa
    
    for sb in range(sa+1, 5, 1):
        if mina > ca[sb]:
            mina = ca[sb]
            minx = sb
    
    temp = ca[sa]
    ca[sa] = ca[minx]
    ca[minx] = temp
    print(ca)