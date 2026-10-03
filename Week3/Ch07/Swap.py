# na = 10
# nb = 11 
# temp = na 

def funca():
    global na, nb
    temp = na
    na = nb
    nb = temp

na=10
nb=11
funca()
print("na 값은", na, "nb 값은", nb)


def funcb(pa,pb):
    temp=pa
    pa=pb
    pb=temp
    return pa, pb

nc=10
nd=11
nc, nd = funcb(nc, nd)
print("nc 값은", nc, "nd 값은", nd)

