for _ in range(int(input())):
    d = list(map(str, input().lower().split()))

    ans = 0
    for i in d:
        if 's' in i:
            ans += 1

    print(ans)