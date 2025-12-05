while True:
    n = int(input())
    if n==0:
        break

    data = list(input() for _ in range(n))
    print(n)
    print(*data)