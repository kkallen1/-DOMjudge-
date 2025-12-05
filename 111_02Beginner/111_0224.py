from collections import deque

a = deque(list(x for x in input()))
b = deque(list(x for x in input()))

ans = deque()
while a or b:
    if a:
        ans.append(a.popleft())
    if b:
        ans.append(b.popleft())

print(*ans, sep="")