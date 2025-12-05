n = input()
s = input()

for i in s:
    if i=="+":
        n = str(int(n) +1)
        n = n[-1] + n[:-1:]
    else:
        n = str(int(n) -1)
        n = n[1::] + n[0]

    if n[0] == '0':
        n = str(int(n))
print(n)