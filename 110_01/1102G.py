currect = list(map(int, input().split()))
for _ in range(int(input())):
    data = list(map(int, input().split()))

    c, d = currect[:], data[:]

    A, B = 0, 0
    for i, j in zip(currect, data):
        if i==j:
            A+=1
            c.remove(i)
            d.remove(j)
    
    for i in set(d):
        B += min(c.count(i), d.count(i))
    
    print(f"{A}A{B}B")