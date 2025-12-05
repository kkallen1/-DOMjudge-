from collections import defaultdict, deque

tree = defaultdict(list)
n = int(input())
ans = [[x, -1, 0, 0, 0] for x in range(n)]

Leaf = []
for _ in range(n):
    a, b, c = map(int, input().split())

    if b==c==-1:
        Leaf.append(a)
        continue

    if b!=-1:
        tree[a].append(b)
        tree[b].append(a)
        ans[a][2] += 1

    if c!=-1:
        tree[a].append(c)
        tree[c].append(a)
        ans[a][2] += 1

queue = deque([ (0, 0) ])
has_been = set()
while queue:
    now, deep = queue.popleft()
    has_been.add(now)
    ans[now][3] = deep

    for node in tree[now]:
        if node not in has_been:
            queue.append( (node, deep+1) )
            ans[node][1] = now

# print(Leaf)
for i in Leaf:
    queue = deque([(i, 0)])

    while queue:
        now, height = queue.popleft()
        ans[now][4] = max(ans[now][4], height)

        if ans[now][1] == -1:
            break
        queue.append( (ans[now][1], height+1) )

for i in ans:
    print(f"node {i[0]}: parent = {i[1]}, degree = {i[2]}, depth = {i[3]}, height = {i[4]},")