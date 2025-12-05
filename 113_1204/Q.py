from collections import defaultdict, deque

n = int(input())
tree = defaultdict(list)
for _ in range(n-1):
    a, b= map(int, input().split())

    tree[a].append(b)
    tree[b].append(a)

ans = []
for i in range(1, n+1):
    queue = deque([[i, 0]])
    has_been = set()
    
    mxd = 0
    while queue:
        now, deep = queue.popleft()
        has_been.add(now)

        mxd = max(mxd, deep)

        for node in tree[now]:
            if node not in has_been:
                queue.append([node, deep+1])
    ans.append(mxd)
print(*ans)