def min_heap():
    for i in range(L//2):
        now = d[i]

        l = i*2+1
        r = i*2+2

        if l<L and r<L:
            if now > d[l] or now > d[r]:
                return False
        elif l<L:
            if now > d[l]:
                return False
    return True

def max_heap():
    for i in range(L//2):
        now = d[i]

        l = i*2+1
        r = i*2+2

        if l<L and r<L:
            if now < d[l] or now < d[r]:
                return False
        elif l<L:
            if now < d[l]:
                return False
    return True

def BST():
    for i in range(L//2):
        now = d[i]

        l = i*2+1
        r = i*2+2

        if l<L and r<L:
            if now < d[l] or d[r] < now:
                return False
        elif l<L:
            if now < d[l]:
                return False
    return True

for _ in range(int(input())):
    d = list(map(int, input().split(',')))

    L = len(d)

    if min_heap() or max_heap():
        print('H')
    elif BST():
        print('B')
    else:
        print('F')