dp = [0, 1, 5, 14]

while True:
    n = int(input())
    if n==0:
        break

    i = len(dp)
    while len(dp)<=n:
        dp.append(dp[-1] + i*i)
        i+=1
    
    print(dp[n])