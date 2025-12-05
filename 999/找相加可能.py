while True:
    try:
        a, b = map(str, input().split())
        a = list(map(int, a.split(',')))
        b = int(b)

        flag = []
        for i in range(len(a)):
            if flag:
                break
            for j in range(i):
                if a[i]+a[j]==b:
                    flag = [j, i]
                    break

        if flag:
            print(*flag)
        else:
            print('F')
    except EOFError:
        break