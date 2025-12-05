for _ in range(int(input())):
    d = list(eval(input()))

    ans = []
    has_been = set()
    for i in range(1, max(d)+1):
        tmp = []
        now = i
        while now not in has_been:
            tmp.append(now)
            has_been.add(now)

            now = d[now-1]
        if tmp:
            ans.append(tmp)
    print(ans)