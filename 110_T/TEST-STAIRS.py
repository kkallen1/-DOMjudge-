n = int(input())

kk = 0
for i in range(n):
    if i%2==0:
        for j in range(n):
            print(' '*(kk*n) + '*')
    else:
        print(' '*(kk*n) + '*' * (n+1))
        kk += 1