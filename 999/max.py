while True:
    try:
        a = list(map(int, input().split()))
        print(max(a))
    except EOFError:
        break