a = int(input())

ans = 0
while a!=0:
    ans += 1

    a = a-1 if a%2!=0 else a//2
print(ans)