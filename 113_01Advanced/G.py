data = []
for _ in range(int(input())):
    a, b = map(int, input().split())

    data.append((a,b))

max = -9999
min = 9999
for i in range(len(data) -1):
    x1, y1 = data[i]
    x2, y2 = data[i+1]

    tmp = abs(x1 - x2) + abs(y1 - y2)
    if tmp > max:
        max = tmp
        
    if tmp < min:
        min = tmp

print(max, min)