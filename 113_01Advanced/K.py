for _ in range(int(input())):
    a, b = map(int, input().split())

    ans = []
    while a//b > 0:
        x = a // b
        y = a % b

        if y<10:
            ans.append(y)
        else:
            ans.append(chr(y+55))

        a = x
    ans.append(a)
    ans = ans[::-1]

    print(*ans, sep="")