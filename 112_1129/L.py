d = []
for i in range(1, int(input())+1):
    d.append(int(input()))
    d.sort()

    if i%2==0:
        print((d[i//2] + d[i//2-1])//2)
    else:
        print(d[i//2])