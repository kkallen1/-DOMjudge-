n = int(input())

tree = [
    []
    for _ in range(n)
]

for _ in range(n-1):
    a, b = map(int, input().split())
    a -=1
    b -=1

    tree[a].append(b)
    tree[b].append(a)

max_deep = 0
for i in range(n):
    has_been = []
    stack = [(i, 0)]

    while stack:
        now, deep = stack.pop(0)
        has_been.append(now)

        if deep > max_deep:
            max_deep = deep

        for i in tree[now]:
            if i not in has_been:
                stack.append((i, deep +1))

print(max_deep)