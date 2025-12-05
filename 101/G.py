for _ in range(int(input())):
    n = input()
    L = len(n)

    n = int(n, 2)

    a = hex(n)[2::]
    if L%4!=0:
        a = (L//4-len(a)+1)*'0' + a
    else:
        a = (L//4-len(a))*'0' + a
    
    b = oct(n)[2::]
    if L%3!=0:
        b = (L//3-len(b)+1)*'0' + b
    else:
        b = (L//3-len(b))*'0' + b
    print(a.upper(), b, sep=",")