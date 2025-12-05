a = [x for x in input()]

a.pop(0)
a.pop()

flag = [1, 1, 1]
for i in range(len(a)-1):
    if a[i+1] > a[i]:
        flag[1] = 0
        flag[2] = 0

    if a[i+1] < a[i]:
        flag[0] = 0
        flag[2] = 0

if flag[0]:
    print(1)
elif flag[1]:
    print(2)
else:
    print(3)