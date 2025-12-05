from collections import deque

a = deque(list(x for x in input()))

# C, C++, C#
ans = [0, 0, 0]
for i in a:
    if i=='#':
        ans[2] += 1
    elif i=='+':
        ans[1] += 1
    else:
        ans[0] += 1

ans[1] //= 2
ans[0] -= ans[1] + ans[2]

print(*ans, sep=",")