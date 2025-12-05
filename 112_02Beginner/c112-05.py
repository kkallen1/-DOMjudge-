d = list(map(str, input().replace(',',' ').replace('.',' ').split()))
d.sort(key=lambda x: len(x))
print(len(d[-1]))