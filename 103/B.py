for _ in range(int(input())):
    a, b, c, d = map(int, input().split(','))

    y = (d-b*a)//(c-b)
    x = a-y
    print(x, y, sep=",")