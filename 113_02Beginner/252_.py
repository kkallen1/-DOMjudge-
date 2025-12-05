data = list(x for x in input())

n = len(data)
if n%2 == 0:
    tmp = []
    for i in range(0, n, 2):
        tmp.append(f"{data[i+1]}{data[i]}")
    
    print(*tmp, sep="")

else:
    tmp = [data.pop(0)]

    for i in range(0, n-1, 2):
        tmp.append(f"{data[i+1]}{data[i]}")
    
    print(*tmp, sep="")