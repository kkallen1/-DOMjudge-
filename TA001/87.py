a, b= map(int, input().split())
a = bin(a)[2::]
b = bin(b)[2::]

a = (20-len(a))*'0' + a
b = (20-len(b))*'0' + b

ans = 0
for i, j in zip(a, b):
    if i!=j:
        ans += 1
print(a)
print(b)
print(ans)