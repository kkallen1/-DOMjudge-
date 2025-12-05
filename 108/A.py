for _ in range(int(input())):
    d = list(map(str, input()))

    ans = 0
    kk = 1
    for i in d:
        if i=='O':
            ans += kk
            kk += 1
        else:
            kk = 1
    print(ans)