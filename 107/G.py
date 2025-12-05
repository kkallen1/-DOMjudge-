from collections import deque, defaultdict

def f(root):
    queue = deque([[root, 0]])
    has_been = set()

    mx_n = None
    mx_d = 0

    while queue:
        now, deep = queue.popleft()

        has_been.add(now)
        
        if deep > mx_d:
            mx_n = now
            mx_d = deep

        for node in tree[now]:
            if node not in has_been:
                queue.append([node, deep+1])

    return mx_n, mx_d

for _ in range(int(input())):
    d = list(map(str, input().strip('[').strip(']').split(',')))

    tree = defaultdict(list)

    L = len(d)
    for i in range(L//2):
        root = d[i]

        if root=='null':
            continue
        
        l = i*2+1
        r = i*2+2

        if l<L and d[l]!='null':
            tree[root].append(d[l])
            tree[d[l]].append(root)
        if r<L and d[r]!='null':
            tree[root].append(d[r])
            tree[d[r]].append(root)
    n1,d1 = f(d[0])
    n2,d2 = f(n1)
    print(d2)