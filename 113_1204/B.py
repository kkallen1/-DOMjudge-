a, b= map(int, input().split())

if a>b:
    a, b= b,a

if a%2!=0:
    a+=1

ans = 0
for i in range(a, b+1, 2):
    ans += i
print(ans)