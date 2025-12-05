for _ in range(int(input())):
    d = list(list(map(int, input())) for _ in range(3))

    if d[0][0] == d[0][1] == d[0][2] and d[0][0]!=0:
        print(d[0][0])
        continue
    if d[1][0] == d[1][1] == d[1][2] and d[1][0]!=0:
        print(d[1][0])
        continue
    if d[2][0] == d[2][1] == d[2][2] and d[2][0]!=0:
        print(d[2][0])
        continue

    if d[0][0] == d[1][0] == d[2][0] and d[0][0]!=0:
        print(d[0][0])
        continue
    if d[0][1] == d[1][1] == d[2][1] and d[0][1]!=0:
        print(d[0][1])
        continue
    if d[0][2] == d[1][2] == d[2][2] and d[0][2]!=0:
        print(d[0][2])
        continue

    if d[0][0] == d[1][1] == d[2][2] and d[0][0]!=0:
        print(d[1][1])
        continue
    if d[0][2] == d[1][1] == d[2][0] and d[0][2]!=0:
        print(d[1][1])
        continue

    print(3)