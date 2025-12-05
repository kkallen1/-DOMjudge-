a= input()
b= input()
c= input()

LA = len(a)
LB = len(b)
LC = len(c)

dp = [[[0]*(LC+1) for _ in range(LB+1)] for __ in range(LA+1)]
for i in range(1, LA+1):
    for j in range(1, LB+1):
        for k in range(1, LC+1):
            if a[i-1]==b[j-1]==c[k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1] +1
            else:
                dp[i][j][k] = max(
                    dp[i-1][j][k],
                    dp[i][j-1][k],
                    dp[i][j][k-1],
                )
print(dp[-1][-1][-1])