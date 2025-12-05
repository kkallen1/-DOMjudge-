n = int(input())
d = set(map(int, input().split()))

d = list(d)
d.sort()
print(len(d))
print(*d)