n, x = map(int, input().split())
coins = [int(x) for x in input().split()]

dp = [float('inf')] * (x+1)
dp[0] = 0
for i in range(1, x+1):
    for coin in coins:
        if coin<=i:
            dp[i] = min(dp[i], dp[i-coin]+1)

if dp[-1] != float('inf'):
    print(dp[-1])
else:
    print(-1)