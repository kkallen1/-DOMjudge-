import sys

for l in sys.stdin:
    n = l.strip()

    ans = int(n[0])
    for i in range(1, len(n)):
        if i%2==0:
            ans -= int(n[i])
        else:
            ans += int(n[i])
    print(ans)