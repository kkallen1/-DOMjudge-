n = int(input())

tmp = []

if n%2==0:
    while n%2==0:
        tmp.append(2)
        n//=2

for i in range(3, n+1, 2):
    if n%i==0:
        while n%i==0:
            tmp.append(i)
            n//=i

kk = {}
for i in set(tmp):
    kk[i] = tmp.count(i)

kk = sorted(kk.items(), key=lambda x: x[0])

ans = []
for i, j in kk:
    if j != 1:
        ans.append(f"{i}^{j}")
    else:
        ans.append(f"{i}")


print(*ans, sep=" * ")