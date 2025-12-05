a = int(input())
b = int(input())

ans = 0
for n in range(a, b+1):
    n = str(n)

    if '0' in n:
        continue

    flag = 1
    for i in n:
        if int(n) % int(i) != 0:
            flag = 0
            break
    
    if flag:
        ans += 1
print(ans)