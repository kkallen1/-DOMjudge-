for _ in range(int(input())):
    n = int(input())
    d=  list(map(int, input().split()))
    target = d.pop()

    flag = 0
    for i in range(n-1):
        for j in range(i):
            if d[i] + d[j] == target:
                flag = 1
                break
        if flag:
            break
    
    if flag:
        print('YES')
    else:
        print('NO')