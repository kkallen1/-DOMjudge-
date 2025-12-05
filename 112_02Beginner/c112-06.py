d = list(map(str, input().replace(',',' ').replace('.',' ').split()))

flag = 1
for i in d:
    if i != i.title() and i != i.lower() and i != i.upper():
        flag = 0
        break
print(flag)