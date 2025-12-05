while True:
    d = list(map(str, input().split()))
    
    if d and d[0]=='0':
        break

    a, b = d

    a = len(b)//int(a)

    ans = []
    for i in range(0, len(b), a):
        ans.append(b[i:i+a:][::-1])

    print(*ans, sep="")