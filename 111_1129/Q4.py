while True:
    try:
        a = list(x for x in input())
        ans = [a[0].lower(), '', a[-1].lower()]

        if len(a)%2 != 0:
            ans[1] = (a[len(a)//2]).lower()
        else:
            ans[1] = (a[len(a)//2-1] + a[len(a)//2]).lower()
        print(*ans, sep=',')
    except EOFError:
        break