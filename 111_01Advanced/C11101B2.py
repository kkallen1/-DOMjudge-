for _ in range(int(input())):
    a = list(int(x) for x in input().split())

    a.sort()
    if a[0]==a[1]==a[2]==a[3]:
        print('square')
    
    elif a[0]==a[1] and a[2]==a[3]:
        print('rectangle')

    elif sum(a[:3:]) >= a[3]:
        print('quadrangle')
    
    else:
        print('banana')
