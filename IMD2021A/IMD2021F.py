x, y = map(str, input().split())

if x.isdigit() and y.isdigit():
    x=int(x)
    y=int(y)
    print(x-y)
else:
    print('NaN')