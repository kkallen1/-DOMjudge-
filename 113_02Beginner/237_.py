a = [int(x) for x in input().split(', ')]

flag = 0
for i in a:
    tmp = 0
    for j in a:
        if j%i==0:
            tmp += 1
    
    if tmp == len(a):
        flag = 1
        break

print(flag)