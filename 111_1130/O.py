a, b= map(int, input().split())
d = list(map(int, input().split()))
d = [x for x in d if x<=b]
d.sort()

dp = [0] * (b+1)
dp[0] =1
for i in d:
    for j in range(i, b+1):
        dp[j] += dp[j-i]
print(dp[-1])