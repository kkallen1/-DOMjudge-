d = list(map(str, input()))

ans = 0
if (d[0] == d[1] == d[2]):
    ans = (d[0])
elif (d[3] == d[4] == d[5]):
    ans = (d[3])
elif (d[6] == d[7] == d[8]):
    ans = (d[6])

elif (d[0] == d[3] == d[6]):
    ans = (d[0])
elif (d[1] == d[4] == d[7]):
    ans = (d[1])
elif (d[2] == d[5] == d[8]):
    ans = (d[2])

elif (d[0] == d[4] == d[8]):
    ans = (d[0])
elif (d[6] == d[4] == d[2]):
    ans = (d[6])

if ans == 'O':
    print(1)
elif ans == 'X':
    print(2)
else:
    print(3)