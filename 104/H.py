from collections import defaultdict, deque

for _ in range(int(input())):
    d = list(map(str, input().split()))

    tree = defaultdict(list)
    mn_n = None
    mn_v = float('inf')

    for i in d:
        a, b, v = i.split(',')
        v = int(v)
        tree[a].append([b, v])
        tree[b].append([a, v])

        if v < mn_v:
            mn_n = a
            mnv = v

    queue = deque([[mn_n, 0]])
    has_been = set()
    
    ans = 0
    while queue:
        now, v = queue.popleft()

        has_been.add(now)
        ans += v

        mn_n = None
        mn_v = float('inf')
        for node in has_been:
            for i in tree[node]:
                if i[0] not in has_been:
                    if i[1]<mn_v:
                        mn_n = i[0]
                        mn_v = i[1]
        
        if mn_n!=None:
            queue.append([mn_n, mn_v])
    
    print(ans)