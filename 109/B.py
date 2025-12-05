for _ in range(int(input())):
    n = input()

    ans = []
    tmp = []
    for i in n[::-1]:
        if i=='4':
            tmp.append('1')
            ans.append(str(int(i) - 1))
        else:
            tmp.append('0')
            ans.append(i)
    
    print(int(''.join(ans[::-1])), int(''.join(tmp[::-1])))