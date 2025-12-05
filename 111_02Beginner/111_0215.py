from collections import deque

x, y = 0, 0
a = deque(list(x for x in input()))

while a:
    tmp = a.popleft()

    if tmp=='U':
        y += 1

    elif tmp=='D':
        y -= 1

    elif tmp=='L':
        x -= 1

    elif tmp=='R':
        x += 1

if x==0 and y==0:
    print('Y')
else:
    print('N')