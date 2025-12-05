while True:
    try:
        a = list(int(x) for x in input().split(','))

        ans = 0
        for i in range(len(a)):
            for j in range(i+1, len(a)):
                if a[i] == a[j]:
                    ans += 1

        print(ans)
    except EOFError:
        break