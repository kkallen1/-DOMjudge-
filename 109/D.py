for _ in range(int(input())):
    n = int(input())

    ans = []
    for i in range(9, 1, -1):
        while n%i==0:
            n//=i
            ans.append(i)
    
    if n==1 and ans:
        print(*ans[::-1], sep="")
    else:
        print(-1)