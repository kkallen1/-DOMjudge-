import sys

for l in sys.stdin:
    d=  list(map(int, l.strip().split(', ')))

    for i in range(2):
        for j in range(len(d)-i-1):
            if d[j] > d[j+1]:
                d[j], d[j+1] = d[j+1], d[j]
        
    print(d)