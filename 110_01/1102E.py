import sys

D = {}
for l in sys.stdin:
    l = l.split()
    if not l:
        break

    D[l[1]] = l[0]

for l in sys.stdin:
    a = l.strip()

    if a in D:
        print(D[a])
    else:
        print('eh')