a = list(x for x in input() if x in ['(', ')'])

mx = 0
now = 0
for i in a:
    if i=='(':
        now += 1
    else:
        mx = max(mx, now)
        now -= 1
print(mx)