for _ in range(int(input())):
    currect, data = map(str, input().split(', '))

    c = [x for x in currect]
    d = [x for x in data]

    A, B = 0, 0

    for i, j in zip(currect, data):
        if i==j:
            A += 1

            # print(c, d, i)
            
            c.remove(i)
            d.remove(j)
    
    # print(c)
    # print(d)
    
    for i in set(d):
        B += min(c.count(i), d.count(i))
    
    print(f"{A}A{B}B")