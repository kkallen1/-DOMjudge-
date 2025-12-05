def f(n, k):
    if n == 0:
        return 0
    if k==0:
        return 1
    if dp[n][k] != -1:
        return dp[n][k]
    
    tmp = 0
    i = 0
    while True:
        if i<n and k-i >= 0:
            tmp += f(n-1, k-i)
            i+=1
        else:
            break
    
    dp[n][k] = tmp
    return dp[n][k]

dp = [[-1]*99 for _ in range(13)]
for _ in range(int(input())):
    n, k = map(int, input().split())

    print(f(n, k))