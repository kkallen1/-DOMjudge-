n = int(input())

ans = [n]
while n!=1:
    if n%2==0 and n>=4:
        n//=4
    elif n%2==0:
        n//=2
    elif n%2!=0:
        n = n*5+1
    
    ans.append(n)

print(*ans, sep="->")