ans = 0
for i in range(5):
    a,b,c= map(int, input().split())

    if (a+b>c) and (a+c>b) and (b+c>a):
        ans+= 1

print(ans)