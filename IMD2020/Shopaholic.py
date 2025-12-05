from collections import deque

for _ in range(int(input())):
    n = int(input())
    data = deque(list(map(int, input().split())))

    data = deque(sorted(data, reverse=True))
    ans = 0
    while len(data) >=3:
        a = data.popleft()
        b = data.popleft()
        c = data.popleft()

        ans += c

    print(ans)