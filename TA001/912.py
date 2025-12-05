d = list(map(int, input().split()))

L = len(d)//3

D = []
idx = 0
for i in range(3):
    tmp = []
    for j in range(L):
        tmp.append(d[idx])
        idx += 1
    D.append(tmp)


ans = []
for i in zip(*D):
    i = list(i)
    i.remove(max(i))
    ans.append(max(i))

print([ans for _ in range(3)])