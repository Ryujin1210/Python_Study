su = [5, 4, 7, 10, 6]

def fmax(fu):
    max = fu[0]
    for sfu in fu:
        if max < sfu:
            max = sfu
    return max
print(fmax(su))


def fmin(fu):
    min = fu[0]
    for sfu in fu:
        if min > sfu:
            min = sfu
    return min
print(fmin(su))

print(max(su))
# def fmax(a,b,c,d,e):
#     fu=[a,b,c,d,e]
#     max = fu[0]
#     for sa in range(1, 5, 1):
#         if max < fu[sa]:
#             max = fu[sa]
#     return max

# a = su[0]
# b = su[1]
# c = su[2]
# d = su[3]
# e = su[4]
# print(fmax(a,b,c,d,e))


# #     max = a
#     if max < b:
#         max = b
#     if max < c:
#         max = c
#     if max < d:
#         max = d
#     if max < e:
#         max = 2
#     return max


# max = fmax(a,b,c,d,e)
# print(max)