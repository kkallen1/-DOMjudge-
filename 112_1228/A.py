while True:
    try:
        a = list(map(str, input().replace('[', '').replace(']', '').split(',')))
        a = [int(x) for x in a]

        if a==sorted(a) or a==sorted(a, reverse=True):
            print('true')
        else:
            print('false')
    except EOFError:
        break