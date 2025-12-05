data = ['A', 'B', 'C', 'D', 'E', 'F']


a = list(x for x in input().replace(" ", ""))

kk = a.count('{')
for _ in range(kk):
    a.remove('{')
    a.remove('}')

for i in a:
    tmp = data.pop(0)

    data.insert(int(i)-1, tmp)

print(*data, sep="")