while True:
    try:
        a, b, c, d, e = map(int, input().split())

        print(56*a+24*b+14*c+6*d+e*2)
    except EOFError:
        break