d = list(list(map(int, input().split())) for _ in range(3))

a = d[0][1] + d[0][2]
b = d[1][0] + d[1][2]
c = d[2][1] + d[2][0]

S = (a+b+c)//2

d[0][0] = S-a
d[1][1] = S-b
d[2][2] = S-c

for i in d:
    print(*i)