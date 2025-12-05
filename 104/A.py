for _ in range(int(input())):
    n = int(input())
    d = list(map(int, input().split(',')))
    
    now = d[0]
    ans=  0    
    for i in d[1::]:
        if now==i:
            pass
        elif now>i:
            ans += (now-i)*10
        else:
            ans += (i-now)*20
        now = i
    print(ans)