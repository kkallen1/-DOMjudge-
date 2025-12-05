from math import isqrt
a = int(input())
ans = []
while a%2==0:
    a//=2
    ans.append(2)

for i in range(3, isqrt(a), 2):
    while a%i==0:
        a//=i
        ans.append(i)

if a!=1:
    ans.append(a)

print(*ans)