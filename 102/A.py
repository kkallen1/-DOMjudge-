for _ in range(int(input())):
    a = list(x for x in input() if x.isdigit())

    if a:
        a = list(set(a))
        a.sort()
        print(*a, sep="")
    else:
        print("N")