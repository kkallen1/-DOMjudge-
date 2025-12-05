from collections import deque

data = list(int(x) for x in input().split())
data.pop()

ans = deque()
for n in data:
    tmp = set()
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            tmp.add(i)
            tmp.add(n//i)
    
    tmp = sum(tmp) - n
    if tmp == n:
        ans.append(f"{n:5d} PERFECT")
    elif tmp < n:
        ans.append(f"{n:5d} DEFICIENT")
    else:
        ans.append(f"{n:5d} ABUNDANT")

print(*ans, sep="\n")