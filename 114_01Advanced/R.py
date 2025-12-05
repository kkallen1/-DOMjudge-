from collections import deque

data = [50, 25, 10, 5, 1]
dp = [0] * 7490
dp[0] = 1

for coin in data:
    for i in range(coin, 7489+1):
        dp[i] += dp[i-coin]

while True:
    try:
        n = int(input())
        print(dp[n])
    except EOFError:
        break