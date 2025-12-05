a = list(int(x) for x in input().split())

a = {
    x: a.count(x)
    for x in a
}

a = sorted(a.items(), key=lambda x:x[1], reverse=True)
print(a[0][0])