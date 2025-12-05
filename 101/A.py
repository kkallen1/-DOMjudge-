import sys

d = []
a = input()
while True:
    tmp = list(input().strip()
                .replace(',','')
                .replace('.','')
                .replace('!','')
                .replace('?','')
                .replace(';','')
                .replace(':','')
                .lower()
                .split()
            )
    if tmp and tmp[0]=='eof':
        break

    d += tmp

ans = d.count(a)
print(ans, len(d), sep=",")