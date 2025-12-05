for _ in range(int(input())):
    D = []
    
    for i in range(int(input())):
        # v, w
        D.append( tuple(map(int, input().split())) )

    # bg
    ans = 0
    for _ in range(int(input())):
        g = int(input())

        dp = [0]*(g+1)

        for v, w in D:
            for i in range(g, w-1, -1):
                dp[i] = max(
                    dp[i],
                    dp[i - w] + v
                )

        # print(dp)
        ans += dp[-1]
    print(ans)