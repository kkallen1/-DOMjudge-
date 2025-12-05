for _ in range(int(input())):
    a,b,c,d,e,f = map(int, input().split())

    ans = 0
    for i in range(a, b+1):
        for j in range(c,d+1):
            for m in range(e, f+1):
                if (i+j)%m == (i-j)%m:
                    ans += 1
    
    print(ans)