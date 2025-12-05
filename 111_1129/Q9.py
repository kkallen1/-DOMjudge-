a = list(x for x in input().split())
a, b = list(map(int, a[0].split(','))), int(a[-1])

ans = 0
flag = 0
for i in range(len(a)):
    if a[i] >= b:
        flag = 1
        ans = i
        break

if flag:
    print(ans)
else:
    print(len(a))