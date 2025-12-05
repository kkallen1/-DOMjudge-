from collections import deque

for _ in range(int(input())):
    n = int(input())
    m = int(input())

    d = [list(map(int, input().split())) for _ in range(n)]

    dp = [[0]*(m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            now = d[i-1][j-1]

            if i==1:
                dp[i][j] = now + dp[i][j-1]
            elif j==1:
                dp[i][j] = now + dp[i-1][j]
            else:
                dp[i][j] = now + min(
                    dp[i-1][j],
                    dp[i][j-1]
                )
    print(dp[-1][-1])