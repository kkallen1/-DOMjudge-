D = {
'00': '0', 
'01': '1', 
'100': '2', 
'101': '3', 
'1100': '4', 
'1101': '5', 
'11100': '6', 
'11101': '7', 
'111100': '8', 
'111101': '9',
}

for _ in range(int(input())):
    n = input()

    ans = ''
    tmp = ''
    for i in n:
        tmp += i
        if tmp in D:
            ans += D[tmp]
            tmp = ''
    
    ans = int(ans)
    if ans in [24,25,26]:
        print(chr(ans+41))
    else:
        print(chr(ans+67))