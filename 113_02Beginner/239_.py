a = [x for x in input()]

ans = ""
x,y = a[0], 0
for i in a:
    if x==i:
        y += 1
    else:
        ans += f"{x}{y}"
        x = i
        y = 1

ans += f"{x}{y}"
print(ans)