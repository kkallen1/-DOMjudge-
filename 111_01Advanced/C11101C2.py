from collections import deque

for _ in range(int(input())):
    a = int(input())

    ans = deque([0 for _ in range(9+1)])
    for i in range(1, a+1):
        for j in str(i):
            ans[int(j)] += 1

    print(*ans)