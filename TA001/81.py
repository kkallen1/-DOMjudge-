n = str(input())

L = len(n)
ans = 0
for i in n:
    ans += pow(int(i), L)
if ans==int(n):
    print(True)
else:
    print(False)