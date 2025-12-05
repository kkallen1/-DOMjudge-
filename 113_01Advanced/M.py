MOD = 10**9 + 7

n = int(input())

a, b = 0, 1
for i in range(n-1):
    a, b = b, (a+b)%MOD
print(b)