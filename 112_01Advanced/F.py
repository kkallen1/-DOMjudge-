while True:
    try:
        w = int(input())
        tmp = 0
        for _ in range(int(input())):
            a, b = map(int, input().split())
            tmp += a*b

        print(tmp//w)
    except EOFError:
        break