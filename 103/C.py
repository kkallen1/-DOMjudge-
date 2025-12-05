for _ in range(int(input())):
    a = set(map(str, input()))
    b = set(map(str, input()))

    d = list(a&b)
    d.sort()
    if d:
        print(*d, sep="")
    else:
        print('N')