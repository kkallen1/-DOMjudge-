n = int(input())
data = [int(x) for x in input().split()]

dp = []
for i in range(n):
    tmp = [1]
    for j in range(i):
        if data[i] > data[j]:
            tmp.append(dp[j]+1)
        
    dp.append(max(tmp))

print(max(dp))