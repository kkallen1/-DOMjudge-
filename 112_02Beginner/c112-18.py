n = int(input())

ans = 0
while n:
    if n%2==0:
        n//=2
        ans += 2
    else:
        n-=1
        ans += 1
print(ans)