def f(n):
    if n in dp or n==2:
        return True
    
    if n<2 or n%2==0:
        return False
    
    for i in range(3, n, 2):
        if n%i==0:
            return False
    
    dp.add(n)
    return True

dp = {2,3,5,7,11,13,17,19}
for _ in range(int(input())):
    a, b= map(int, input().split(','))

    if abs(a-b)!=2:
        print('N')
        continue

    if f(a) and f(b):
        print('Y')
    else:
        print('N')