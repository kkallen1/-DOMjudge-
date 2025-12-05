while True:
    try:
        a = list(x for x in input())
        b = list(x for x in input())

        tmp = list(set(a) & set(b))

        ans = []
        for i in tmp:
            k1 = a.count(i)
            k2 = b.count(i)

            ans.append(i*k1 if k1<k2 else i*k2)
        
        ans.sort()
        print(*ans, sep="")
    except EOFError:
        break