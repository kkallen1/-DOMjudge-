n = int(input())
for _ in range(n):
    # start, end
    x1, y1, x2, y2 = map(int, input().split())

    if x1==x2 and y1==y2:
        print(0)
        continue

    if (
        (x1==x2) or
        (y1==y2) or
        (abs(x1-x2) == abs(y1-y2))
    ):
        print(1)
        continue

    print(2)