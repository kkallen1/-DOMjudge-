from collections import deque, defaultdict

for _ in range(int(input())):
    m = int(input())

    tree = defaultdict(list)
    for _ in range(m-1):
        a,b =map(int, input().split(','))
        tree[a].append(b)
        tree[b].append(a)
    
    queue = deque([[0, 0]])
    dp = set()

    ans = 0
    while queue:
        now, deep = queue.popleft()

        dp.add(now)
        ans =max(ans, deep)

        for node in tree[now]:
            if node not in dp:
                queue.append([node, deep+1])
    
    print(ans+1)
    try:
        _ = input()
    except:
        break