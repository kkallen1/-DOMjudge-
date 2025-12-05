n = int(input())
ans = []
while n!=1:
    ans.append(n)
    if n%2==0:
        n//=2
    else:
        n = n*3+1
print(*ans, n)