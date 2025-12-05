for _ in range(int(input())):
    a, b= map(int, input().split())
    d = list(map(int, input().split()))

    d.sort()

    ans = 0
    tmp = []
    for i in range(a-1, -1, -1):
        tmp.append(d.pop())
        if min(tmp) * len(tmp) >= b:
            ans += 1
            tmp = []
    
    print(ans)