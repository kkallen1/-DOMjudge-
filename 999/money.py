while True:
    try:
        x, y, z = map(int, input().split())

        A = (x-y+z)//2
        J = z-A
        B = y-J

        print(A, B, J)
    except EOFError:
        break