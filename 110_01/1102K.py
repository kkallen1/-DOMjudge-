while True:
    a = int(input())
    b = int(input())
    c = int(input())

    print(pow(a,b,c))
    try:
        _ = input()
    except:
        break