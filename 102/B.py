import itertools

for _ in range(int(input())):
    data = []
    for __ in range(int(input())):
        data += [int(x) for x in input().split(',')]

    count = 0
    ans = []
    for i in set(data):
        tmp = data.count(i)

        if tmp > count:
            count = tmp
            ans = [i]
        elif tmp == count:
            ans.append(i)
    
    ans.sort()
    for i in range(len(ans)):
        if len(str(ans[i]))<2:
            ans[i] = f"0{ans[i]}"
    print(*ans, sep=', ')
    try:
        _ = input()
    except:
        break