n = int(input())
d = list(map(int, input().split()))

ans = sum(d)
if ans%2==0:
    print(ans)
else:
    d.sort(key=lambda x: (x%2==0, x))
    print(ans-d[0])