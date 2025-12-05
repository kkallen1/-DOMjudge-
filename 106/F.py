for _ in range(int(input())):
    d = list(map(int, input().split(', ')))

    S = sorted(d)
    ans = []
    for i in d:
        ans.append(S.index(i)+1)
    
    print(*ans, sep=', ')