for _ in range(int(input())):
    a = list(map(str, input()))
    b = list(map(str, input()))

    LA = len(a)
    LB = len(b)

    dp = [[0]*(LB+1) for _ in range(LA+1)]

    for i in range(1, LA+1):
        for j in range(1, LB+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] +1
            else:
                dp[i][j] = max(
                    dp[i-1][j],
                    dp[i][j-1]
                )
    
    print(dp[-1][-1])