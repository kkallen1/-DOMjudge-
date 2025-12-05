for _ in range(int(input())):
    d = list(map(str, input().split()))
    d = [int(d[x] + d[x+1], 16) for ｘ in range(0, 20, 2)]

    d = hex(sum(d))[2::]
    if len(d)>4:
        d = int(d[0], 16) + int(d[1::], 16)
        d = hex(d)[2::]

    d = int(d, 16)
    d = ~d & 0xFFFF
    d = hex(d)[2::]
    print('0'*(4-len(d)) + d)