import sys

# for _ in range(int(input())):
#     a, b=  map(int, input().split())
idx = 1
for l in sys.stdin:
    a, b=  map(int, l.split())
    if a==b==0:
        break

    a1 = list(map(int, input().split()))
    b1 = list(map(int, input().split()))

    dp = [[0]*(b+1) for _ in range(a+1)]
    for i in range(1, a+1):
        for j in range(1, b+1):
            if a1[i-1] == b1[j-1]:
                dp[i][j] = dp[i-1][j-1] +1
            else:
                dp[i][j] = max(
                    dp[i][j-1],
                    dp[i-1][j],
                )
    # print(dp)
    print(f"Twin Towers #{idx}")
    print(f"Number of Tiles : {dp[-1][-1]}")
    print()
    idx += 1