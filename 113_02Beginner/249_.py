a, b = map(str, input().split(', '))

count = [
    [
        a.count('E'),
        a.count('A'),
        a.count('C'),
    ],
    [
        b.count('E'),
        b.count('A'),
        b.count('C'),
    ],
]

total_count = 0
sum = 0
for i in range(2):
    for j in range(3):
        total_count += count[i][j]
        
        if j==1:
            sum += count[i][j] * 800

sum += count[0][0] * 500
sum += count[0][2] * 200

sum += count[1][0] * 400
sum += count[1][2] * 100

if total_count>=20:
    sum *= 0.9
    print(int(sum))
else:
    print(int(sum))