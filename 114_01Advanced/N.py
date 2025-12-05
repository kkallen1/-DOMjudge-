n, k = map(int, input().split())
data = list(int(x) for x in input().split())

ans = -float('inf')
tmp = sum(data[:k:])
for i in range(0, n-k):
    if tmp > ans:
        ans = tmp
    
    tmp -= data[i]
    tmp += data[k+i]
    
    if tmp > ans:
        ans = tmp

print(ans)