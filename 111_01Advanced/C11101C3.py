from collections import deque
while True:
    a, b = input().split()

    if a=='0' and b=='0':
        break
    
    a = deque([int(x) for x in a])
    b = deque([int(x) for x in b])


    ans = 0
    tmp = 0
    while a or b:
        if a:
            i = a.pop()
        else:
            i = 0

        if b:
            j = b.pop()
        else:
            j = 0

        if i + j + tmp > 9:
            ans += 1
            tmp = 1
        else:
            tmp = 0
    
    if ans==1:
        print(f"{ans} carry operation.")
    elif ans>1:
        print(f"{ans} carry operations.")
    else:
        print('No carry operation.')