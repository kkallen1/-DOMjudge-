import itertools

for _ in range(int(input())):
    d = list(map(int, input().split(',')))
    i = d[1]-1
    j = d[2]-1

    d = list(itertools.permutations(str(d[0]), len(str(d[0]))))
    i = ''.join(d[i])
    j = ''.join(d[j])
    print(int(i)+int(j))