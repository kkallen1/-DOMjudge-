n = int(input())

tmp = set()
ans = 0
for i in range(1, n):
    if n%i==0 and i not in tmp:
        ans += i
        ans += n//i
        tmp.add(i)
        tmp.add(n//i)

if ans-n==n:
    print(True)
else:
    print(False)