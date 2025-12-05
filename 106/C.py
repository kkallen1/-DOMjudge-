for _ in range(int(input())):
    d = list(map(int, input()))
    
    ans = 0
    for i in range(16):
        if i%2==0:
            tmp = d[i]*2
            if tmp>9:
                tmp = int(str(tmp)[0]) + int(str(tmp)[1])
            
            ans += tmp
        else:
            ans += d[i]
    print('T' if ans%10==0 else 'F')