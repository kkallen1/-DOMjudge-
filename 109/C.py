for _ in range(int(input())):
    d1, m1, y1 = map(int, input().split('/'))
    d2, m2, y2 = map(int, input().split('/'))

    year = y1-y2
    if m1==m2 and d1<d2:
        year -= 1
    elif m1<m2:
        year -= 1
    
    print(year)