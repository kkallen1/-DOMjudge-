n = int(input())
data = [int(x) for x in input().split()]

dp = [0] * n
for i in range(n):
    for j in range(i):
        if data[j] < data[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp)+1)