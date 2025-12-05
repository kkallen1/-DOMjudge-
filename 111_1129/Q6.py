from collections import deque

a = deque(list(int(x) for x in input().split(',')))
tmp = a.count(0)

now = 0
while tmp:
    # print(now, tmp, a)
    if a[now] != 0:
        now += 1
    else:
        a.remove(0)
        a.append(0)
        tmp -= 1
print(*a, sep=",")