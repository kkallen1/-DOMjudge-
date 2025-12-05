a, b= map(str, input().split())
if a==b:
    print(0)
else:
    if (a=='O' and b=='Y') or (a=='Y' and b=='X') or (a=='X' and b=='O'):
        print(1)
    else:
        print(2)