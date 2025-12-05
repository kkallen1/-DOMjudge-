for _ in range(int(input())):
    a, b=  map(str, input().split('/'))
    a = list(map(int, a.split('.')))
    b = list(map(int, b.split('.')))

    ans = []
    for i, j in zip(a,b):
        ans.append( i | (~j & 255) )
    
    print(*ans, sep=".")