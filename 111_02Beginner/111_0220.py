a = list(int(x) for x in input())

ans = sum(a) % 10
ans = 0 if ans==0 else 10-ans
print(*a, ans, sep="")