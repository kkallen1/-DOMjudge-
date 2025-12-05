from collections import defaultdict

for _ in range(int(input())):
    m,r,r,n = map(int, input().split(','))

    A = [list(map(int, input().split())) for _ in range(m)]
    B = [list(map(int, input().split())) for _ in range(r)]
    C = [list(map(int, input().split())) for _ in range(m)]

    x, y = -1, -1
    flag = 0
    for i in range(m):
        for j in range(r):
            if A[i][j] == 9999:
                x = i
                y = j
                flag = 'A'
                break

        if flag:
            break
    
    if x==-1 and y==-1:
        for i in range(r):
            for j in range(n):
                if B[i][j] == 9999:
                    x = i
                    y = j
                    flag = 'B'
                    break

            if flag:
                break
    

    if flag=='A':
        ans = defaultdict(int)
        i = x
        for j in range(n):
            tmp = 0
            for k in range(r):
                if A[i][k]!=9999:
                    tmp += A[i][k] * B[k][j]

            if B[y][j]==0:
                ans[ (C[i][j]-tmp) ] += 1
            else:
                ans[ (C[i][j]-tmp)//B[y][j] ] += 1

        print(max(ans.items(), key=lambda x: x[1])[0])
    else:
        ans = defaultdict(int)
        j = y
        for i in range(m):
            tmp = 0
            for k in range(r):
                if B[k][j]!=9999:
                    tmp += A[i][k] * B[k][j]

            if A[i][x]==0:
                ans[ (C[i][j]-tmp) ] += 1
            else:
                ans[ (C[i][j]-tmp)//A[i][x] ] += 1

        print(max(ans.items(), key=lambda x: x[1])[0])