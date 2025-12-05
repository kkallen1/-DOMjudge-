from collections import deque

while True:
    try:
        data = deque()
        while True:
            a = deque(list(
                x for x in input().split()
            ))

            if a[-1] == '()':
                a.pop()
                data += list(x.replace('(', '').replace(')', '').split(',') for x in a)
                break
            
            data += list(x.replace('(', '').replace(')', '').split(',') for x in a)

        data = deque(sorted(data, key=lambda x: ( len(x[1]), x[1] )))
        # print(data)
        
        path = deque(list( x[1] for x in data ))
        path = deque(sorted(path))
        flag = 1
        for now in path:
            if not flag:
                break

            for i in range(1, len(now)):
                if now[:i] not in path:
                    flag = 0
                    break

        root = data.popleft()

        if root[1] or not flag:
            print('not complete')
            continue

        last = ''
        flag = 1

        ans = deque([root[0]])
        while data:
            now = data.popleft()
            
            if now[1] == last:
                flag = 0
                break
            
            last = now[1]

            ans.append(now[0])
        
        if flag:
            print(*ans)
        else:
            print('not complete')

    except EOFError:
        break