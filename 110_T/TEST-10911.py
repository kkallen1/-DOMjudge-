def f(n):
    if n in dp:
        return True
    
    if n<2 or n%2==0:
        return False
    
    for i in range(3, n, 2):
        if n%i==0:
            return False
    
    dp.append(n)
    return True

dp = [2, 3, 5, 7, 11, 13, 17]

for _ in range(int(input())):
    n = int(input())

    if n>3 and n%2!=0:
        n -= 1

    for i in range(n-1, 1, -2):
        if f(i):
            print(i)
            break