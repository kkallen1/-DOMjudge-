dp = [1, 2]

for _ in range(int(input())):
    n = int(input())
    tmp = n

    while dp[-1]<n:
        dp.append(dp[-1] + dp[-2])

    ans = []
    for i in range(len(dp)-1, -1, -1):
        if n>=dp[i]:
            ans.append('1')
            n -= dp[i]
        else:
            ans.append('0')
    
    print(f"{tmp}={int(''.join(ans))}")