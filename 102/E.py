from collections import deque

for _ in range(int(input())):
    m, k = map(int, input().split(','))

    tree = [
        []
        for __ in range(m)
    ]

    root = None
    for __ in range(m):
        a, b = map(int, input().split(','))
        
        if b==99:
            root = a
        else:
            tree[b].append(a)
    ans = 0

    stack = deque([ [root, 0] ])

    while stack:
        now, deep = stack.popleft()

        if deep == k:
            ans += 1

        for node in tree[now]:
            stack.append([node, deep+1])
    
    print(ans)

    try:
        __ = input()
    except EOFError:
        break