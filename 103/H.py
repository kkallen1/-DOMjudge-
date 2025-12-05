from collections import deque

for _ in range(int(input())):
    m, k, v = map(int, input().split(','))

    Tree = [[[] for _ in range(m)] for _ in range(k)]
    Root = []

    for _ in range(m):
        d = list(map(int, input().split()))
        root = d[0]

        for i in range(k):
            if d[i+1] != 999:
                Tree[i][root].append(d[i+1])
                Tree[i][d[i+1]].append(root)
            else:
                Root.append(root)
    
    ans = []
    for i in range(k):
        queue = deque([[ Root[i], 0 ]])
        has_been = set()

        flag = 0
        while queue:
            now, deep = queue.popleft()

            has_been.add(now)
            
            for node in Tree[i][now]:
                if node == v:
                    flag = 1
                    ans.append(deep+1)
                    break
                if node not in has_been:
                    queue.append([node, deep+1])
            
            if flag:
                break
    print(*ans, sep=',')