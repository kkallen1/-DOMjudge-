data = {}

for _ in range(int(input())):
    tmp = list(x for x in input().split())
    a = int(tmp.pop(0))
    b = int(tmp.pop(0))
    c = int(tmp.pop(0))
    tmp = " ".join(tmp)

    data[tmp] = [a, b, c]

data = sorted(data.items(), key=lambda x: (x[1][0], x[1][1], x[1][2]), reverse=True)
print(data[0][0])