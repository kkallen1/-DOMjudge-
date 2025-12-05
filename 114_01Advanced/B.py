a, b = map(str, input().split())

if a=='Y':
    a = 0
if a=='O':
    a = 1
if a=='X':
    a = 2

if b=='Y':
    b = 0
if b=='O':
    b = 1
if b=='X':
    b = 2

if a==b:
    print(0)
elif (a==0 and b==2) or (a==1 and b==0) or (a==2 and b==1):
    print(1)
else:
    print(2)