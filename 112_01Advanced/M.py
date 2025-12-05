for idx in range(int(input())):
    n = str(input())
    kk = n

    dp = []
    while (n not in dp) and (n!='1'):
        dp.append(n)

        tmp = 0
        for i in n:
            i = int(i)
            tmp += i*i
        
        n = str(tmp)
    
    if n=='1':
        print(f"Case #{idx+1}: {kk} is a Happy number.")
    else:
        print(f"Case #{idx+1}: {kk} is an Unhappy number.")