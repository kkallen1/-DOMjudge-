a = list(x for x in input())

a.sort(key=lambda x:ord(x), reverse=True)

print(a[len(a)//2])