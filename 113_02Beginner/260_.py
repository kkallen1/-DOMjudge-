n = int(input())
data = list(range(1, n+1))

kk = (n*(n+1)) // 2
if kk%2 != 0:
    print("NO")
else:
    kk //= 2
    a, b = [], []

    for i in range(n, 0, -1):
        if sum(a)+i <= kk:
            a.append(i)
        else:
            b.append(i)

    a.sort()
    b.sort()
    print("YES,[", end="")
    print(*a, sep=",", end="")
    print("],[", end="")
    print(*b, sep=",", end="")
    print("]")