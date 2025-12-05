a = input().split('=')

for i in range(1, 100):
    if int(eval( a[0].replace('X', str(i))) ) == int(a[1]):
        print(i)
        break