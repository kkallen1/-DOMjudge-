from collections import deque, defaultdict

n, m = map(int, input().split())

tree = defaultdict(list)
for _ in range(m):
    a, b= map(int, input().split())
    tree[a].append(b)

a, b = map(int, input().split())

queue = deque([a])
has_been = set()

flag = 0
while queue:
    now = queue.popleft()

    has_been.add(now)

    for node in tree[now]:
        if node == b:
            flag = 1
            break
        if node not in has_been:
            queue.append(node)

    if flag:
        break

if flag:
    print('Yes')
else:
    print('No')