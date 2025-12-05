a, b= map(int, input().split())
d = list(map(int, input().split()))

L = a//2
for _ in range(b):
    a = d[:L:]
    b = d[L::]

    d=  []
    for i, j in zip(a, b):
        d.append(i)
        d.append(j)

print(*d)