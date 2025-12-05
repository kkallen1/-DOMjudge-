import sys

for l in sys.stdin:
    d = list(map(int, l.split()))
    n = d[0]

    d = d[2::]
    d.sort(reverse=True)
    dp = [0]*(n+1)
    dp[0] = 1

    for i in d:
        for j in range(n, i-1, -1):
            if dp[j-i]:
                dp[j] = 1
    
    for i in range(n, -1, -1):
        if dp[i]:
            print(i)
            break