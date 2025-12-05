while True:
    try:
        a = list(x for x in input().split())
        a, b = list(map(int, a[0].split(','))), int(a[-1])

        flag = 0
        for i in range(len(a)):
            if flag:
                break

            for j in range(len(a)):
                if i == j:
                    continue
                
                if a[i] + a[j] == b:
                    flag = 1
                    ans = [i, j]
                    break

        print(*ans, sep=',')
    except EOFError:
        break