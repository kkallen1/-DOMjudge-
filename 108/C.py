for _ in range(int(input())):
    a,b,n = map(int, input().split())

    n = str(n)
    ans = 0
    for i in range(a, b+1):
        if n in str(i):
            ans += 1
    print(ans)