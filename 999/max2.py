a, b = map(int, input().split())
d = [list(map(int, input().split())) for _ in range(a)]

mx = -float('inf')
for i in d:
    if max(i) > mx:
        mx = max(i)

print(mx)