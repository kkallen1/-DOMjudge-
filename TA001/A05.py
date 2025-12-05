import sys

for l in sys.stdin:
    x,y,z= map(int, l.split())
    
    j = (z-x+y)//2
    b = y-j
    a = x-b
    print(a,b,j)