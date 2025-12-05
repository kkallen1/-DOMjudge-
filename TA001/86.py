n =input()

dp = set()
while n!='1' and n not in dp:
    dp.add(n)

    tmp = []
    for i in n:
        tmp.append(int(i)*int(i))
    
    n = str(sum(tmp))
if n=='1':
    print(True)
else:
    print(False)