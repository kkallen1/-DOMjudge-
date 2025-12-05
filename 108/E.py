for _ in range(int(input())):
    a,b = map(int, input().split())
    d = [list(map(str, input())) for _ in range(a)]

    ans = []
    for i in zip(*d):
        i = sorted(set(i), key=lambda x: (i.count(x), -ord(x)), reverse=True)

        ans.append(i[0])
    print(*ans, sep="")