from collections import Counter
a = list(map(str, input()))
a = Counter(a)

a = sorted(a.items(), key=lambda x: (x[1], -ord(x[0])))
for i in a:
    print(ord(i[0]), i[1])