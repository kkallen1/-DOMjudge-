for _ in range(int(input())):
    a = list(map(str, input().lower().split()))

    ans = 0
    for i in a:
        if 's' in i:
            ans += 1
    
    print(len(a), ans, sep=',')