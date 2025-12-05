for _ in range(int(input())):
    d = list(map(int, input().split()))

    ans = d[0]
    now = d[0]

    for i in d[1::]:
        now = max(now+i, i)
        ans = max(ans, now)

    ans = max(ans, now)
    print(ans)