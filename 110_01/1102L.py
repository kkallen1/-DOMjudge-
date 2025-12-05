import sys

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
for l in sys.stdin:
    n, c = map(int, l.split())

    ans = {1, }
    for i in range(1, n+1):
        if f(i):
            ans.add(i)
        if f(n//i):
            ans.add(n//i)
    ans = list(ans)
    ans.sort()
    L = len(ans)
    if L%2==0:
        L//=2
        print(f"{n} {c}:", *ans[L-c:L+c:], sep=" ")
    else:
        L//=2
        print(f"{n} {c}:", *ans[L-c+1:L+c:], sep=" ")