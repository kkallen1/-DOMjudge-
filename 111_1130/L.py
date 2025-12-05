a= int(input())

ans = 0
for i in range(1, a+1):
    ans += bin(i).count('1')
print(ans)