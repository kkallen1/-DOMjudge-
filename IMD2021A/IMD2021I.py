while True:
    n = int(input())

    if n==0:
        break

    data = list(int(input()) for _ in range(n))

    ans = 0
    for i in range(n):
        for j in range(i):
            if data[j] > data[i]:
                ans += 1

    print(ans)