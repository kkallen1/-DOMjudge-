from collections import deque, defaultdict

while True:
    n = int(input())
    if n==0:
        break

    Tree = defaultdict(list)
    while True:
        d = list(map(int, input().split()))
        if d[0] == 0:
            break

        root = d[0]
        
        for i in d[1::]:
            Tree[root].append(i)
            Tree[i].append(root)
    
    
    Node = [x for x in Tree if len(Tree[x])>1]
    ans = 0
    for i in Node:
        node = Tree[i][:]

        queue = deque([node[0]])
        has_been = set()
        
        node.remove(node[0])
        while queue:
            now = queue.popleft()

            has_been.add(now)
            if now in node:
                node.remove(now)

            for n in Tree[now]:
                if n==i:
                    continue
                if n not in has_been:
                    queue.append(n)
        
        if len(node)!=0:
            ans += 1

    print(ans)