import sys

for l in sys.stdin:
    a, b= map(int, l.split())
    b /= 100
    print(round(a / pow(b, 2), 2))