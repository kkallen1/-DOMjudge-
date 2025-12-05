from collections import deque, defaultdict

n = int(input())
tree =defaultdict(list)

for _ in range(n-1):
    a,b = map(int, input().split())
    
    tree[a].append(b)
    tree[b].append(a)

def f(root):
    queue = deque([[root, 0]])
    has_been =set()

    mx_n = None
    mx_d = 0

    while queue:
        now, deep = queue.popleft()

        has_been.add(now)
    
        if mx_d < deep:
            mx_d = deep
            mx_n = now

        for node in tree[now]:
            if node not in has_been:
                queue.append([node, deep+1])

    return mx_n, mx_d

n, d = f(1)
n1, d1 = f(n)
print(d1)