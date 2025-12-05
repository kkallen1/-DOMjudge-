n, q = map(int, input().split())
d = list(map(int, input().split()))

for i in range(q):
    a, b = map(int, input().split())
    print(len(set(d[a-1:b])))