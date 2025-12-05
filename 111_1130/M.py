n = int(input())

d = ['0', '1']
for _ in range(n-1):
    a = d
    b = d[::-1]

    d = []
    for i in a:
        d.append('0' + i)
    for i in b:
        d.append('1' + i)

print(*d, sep="\n")