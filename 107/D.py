import itertools

for _ in range(int(input())):
    d = list(map(str, input().split(',')))
    k = int(d.pop())-1
    d = list(itertools.permutations(d[1::], int(d[0])))
    print(''.join(d[k]))