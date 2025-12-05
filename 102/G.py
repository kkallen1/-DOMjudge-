for _ in range(int(input())):
    d = input().replace('-', '')

    if len(d)==10:
        S = 0
        kk = 10
        for i in d[:-1:]:
            S += int(i)*kk
            kk-=1
        S %= 11
        S = 11-S
        if (
            (S==10 and d[-1]=='X') or
            (S==11 and d[-1]=='0') or
            (str(S)==d[-1])
        ):
            print('T')
        else:
            print('F')

    elif len(d)==13:
        S = 0
        for i in range(12):
            if i%2==0:
                S += int(d[i])
            else:
                S += int(d[i]) * 3
        S %= 10
        S = 10-S
        if (
            (S==10 and d[-1]=='0') or
            (str(S)==d[-1])
        ):
            print('T')
        else:
            print('F')