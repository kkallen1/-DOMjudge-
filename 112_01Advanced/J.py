import sys

dp = [1, 2, 4]
for n in sys.stdin:
    n = int(n)

    kk = len(dp)
    while len(dp)<n:
        dp.append(dp[-1] + kk)
        kk += 1
    
    print(dp[n-1])