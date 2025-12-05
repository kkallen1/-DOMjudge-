data = []
# 同花順; 順子
for i in range(1, 52+1, 13):
    for j in range(i, i+9):
        data.append( [j, j+1, j+2, j+3, j+4] )
data.append([1,10,11,12,13])
data.append([1+13,10+13,11+13,12+13,13+13])
data.append([1+26,10+26,11+26,12+26,13+26])
data.append([1+39,10+39,11+39,12+39,13+39])
# print(data)

for _ in range(int(input())):
    a = list(int(x) for x in input().split())

    a.sort()
    if a in data:
        print('同花順')
        continue

    for i in range(5):
        while a[i]>13:
            a[i] -= 13
    
    a.sort()
    if a in data:
        print('順子')
        continue

    count = {}
    for i in set(a):
        count[i] = a.count(i)
    
    # print(a)
    # print(count)

    kk = [0, 0, 0]
    for key, item in count.items():
        if item==4:
            kk[0] += 1
            break
        elif item==3:
            kk[1] += 1
        elif item==2:
            kk[2] += 1

    if kk[0]:
        print('四條')
        continue
    
    if kk[1] and kk[2]:
        print('葫蘆')
        continue

    if kk[1]:
        print('三條')
        continue
    
    if kk[2] == 2:
        print('兩對')
        continue
    
    if kk[2] == 1:
        print('一對')
        continue

    print('雜牌')