correct = list(x for x in input().split())

for _ in range(int(input())):
    data = list(x for x in input().split())
    c = correct[:]
    d = data[:]

    A, B = 0, 0
    idx = 0
    for i, j in zip(correct, data):
        if i==j:
            c.pop(idx)
            d.pop(idx)
            A += 1
        else:
            idx += 1

    for i in set(c):
        B += min(c.count(i), d.count(i))

    print(f"{A}A{B}B")