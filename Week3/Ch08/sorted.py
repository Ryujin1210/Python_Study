ca = [21, 10, 11, 15, 13]

def fselsort(lst):
    for sa in range(0, len(ca)-1):
        mina = ca[sa]
        minx = sa
    
        for sb in range(sa+1, len(ca), 1):
            if mina > ca[sb]:
                mina = ca[sb]
                minx = sb
    
        print(ca)
        ca[sa], ca[minx] = ca[minx], ca[sa]
    return ca

print(fselsort(ca))