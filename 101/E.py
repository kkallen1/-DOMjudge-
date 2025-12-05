D = {'A': '1+0*9', 'B': '1+1*9', 'C': '1+2*9', 'D': '1+3*9', 'E': '1+4*9', 'F': '1+5*9', 'G': '1+6*9', 'H': '1+7*9', 'I': '3+4*9', 'J': '1+8*9', 'K': '1+9*9', 'L': '2+0*9', 'M': '2+1*9', 'N': '2+2*9', 'O': '3+5*9', 'P': '2+3*9', 'Q': '2+4*9', 'R': '2+5*9', 'S': '2+6*9', 'T': '2+7*9', 'U': '2+8*9', 'V': '2+9*9', 'W': '3+2*9', 'X': '3+0*9', 'Y': '3+1*9', 'Z': '3+3*9'}

ans = [0,0,0]
dp = set()
for _ in range(int(input())):
    a = input()
    
    if a in dp:
        ans[1] += 1
        continue

    if a[1] not in '12':
        ans[2] += 1
        continue

    tmp = int(eval(D[a[0]]))
    kk = 8
    
    for i in a[1::]:
        if kk>1:
            tmp += int(i)*kk
            kk -=1
        else:
            tmp += int(i)

    if tmp%10==0:
        ans[0] += 1
        dp.add(a)
    else:
        ans[2] +=1
print(*ans, sep=",")