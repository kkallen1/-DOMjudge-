import sys

for l in sys.stdin:
    n = int(l)

    print(f"C={int((n-32)*5/9)}")