for _ in range(int(input())):
    n = int(input())

    dp = set()
    while n!=1 and n not in dp:
        dp.add(n)
        n = sum([int(x)*int(x) for x in str(n)])
    
    if n==1:
        print('T')
    else:
        print('F')