n = int(input())
data = [int(x) for x in input().split()]

mx = 0
now = 0
for i in data:
    now = max(i, now + i)
    mx = max(mx, now)

print(mx)