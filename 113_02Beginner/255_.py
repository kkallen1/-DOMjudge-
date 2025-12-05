a = list(x for x in input())

ans = 0
stack = []

for i in a:
    if i=='(':
        stack.append(i)
    if i==')' and stack:
        ans += 1
        stack.pop()
print(ans*2)