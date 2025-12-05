n = list(int(x) for x in input())[::-1]

ans = []
for i in range(len(n)):
    if n[i]%2!=0:
        ans = n[i::][::-1]
        break

if ans:
    print(*ans, sep="")
else:
    print(0)