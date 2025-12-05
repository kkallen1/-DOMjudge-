a, b= map(int, input().split())
d = tuple(map(int, input().split()) for _ in range(a))
for i in zip(*d):
    print(*i)