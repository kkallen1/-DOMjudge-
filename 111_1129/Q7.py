a = list(x.lower() for x in input().split())

count = {
    x: a.count(x)
    for x in a
}

count = sorted(count.items(), key=lambda x: x[1], reverse=True)
if count[0][1] != count[1][1]:
    print(*count[0])
else:
    print('No')