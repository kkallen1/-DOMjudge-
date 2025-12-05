import sys
from collections import defaultdict, deque

input = sys.stdin.readline

for _ in range(int(input())):
    v = int(input())
    
    tree = defaultdict(list)
    for _ in range(int(input())):
        a, b = map(int, input().strip().split())

        tree[a].append(b)
        tree[b].append(a)
    
    queue = deque([b])
    color = [0]*v
    color[b] = 1

    flag = 1
    while queue:
        now = queue.popleft()

        next_color = 1 if color[now]==2 else 2

        for node in tree[now]:
            if color[node]==0:
                color[node] = next_color
                queue.append(node)
            elif color[node] != next_color:
                flag = 0
                break
    
        if not flag:
            break
    
    if flag:
        print('T')
    else:
        print('F')