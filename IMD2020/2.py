while True:
    try:
        a = list(x for x in input())[::-1]

        ans = []
        for i in a:
            if i not in ans:
                ans.append(i)
        print(*ans[::-1], sep='')
    except EOFError:
        break