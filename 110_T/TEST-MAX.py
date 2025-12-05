tmp = {}
for _ in range(int(input())):
    a, b = map(str, input().split('>'))

    if a not in tmp:
        tmp[a] = 0

    if b in tmp:
        tmp[b] += 1
    else:
        tmp[b] = 1

Min = min(tmp.items(), key=lambda x: x[1])[1]
# print(Min)

if Min == 0:
    tmp = sorted(tmp.items(), key=lambda x: (x[1], x[0]))
    # print(tmp)

    ans = []
    for i in tmp:
        if i[1]==0:
            ans.append(i[0])
    print(*ans, sep=",")
else:
    print(None)