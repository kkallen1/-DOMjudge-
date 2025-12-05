h1, m1, h2, m2 = map(int, input().split())
while h1!=0 or h2!=0 or m1!=0 or m2!=0:
    D, H, M = 0, 0, 0

    if m1 > m2:
        m2 += 60
        h2 -= 1

        if h2<0:
            h2 += 24

    if h1 > h2:
        h2 += 24
        D += 1

    H = h2-h1
    M = m2-m1

    if D!=1 or D!=0:
        print(H*60 + M)
    else:
        print(D*24*60 + H*60 + M)
    
    h1, m1, h2, m2 = map(int, input().split())