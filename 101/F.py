D = {
    '00': 'A',
    '01': 'B',
    '100': '0', 
    '101': '1', 
    '1100': '2', 
    '1101': '3', 
    '11100': '4',
    '11101': '5',
    '111100': '6', 
    '111101': '7', 
    '111110': '8', 
    '111111': '9',
}

for _ in range(int(input())):
    a = input()

    ans = []
    tmp = []
    for i in a:
        tmp.append(i)
        
        kk = D.get(''.join(tmp), '')
        if kk!='':
            ans.append(kk)
            tmp = []
    
    ans = [''.join(ans[:4:]), ''.join(ans[4::])]
    print(*ans, sep=",")