while True:
    a = bin(int(input()))[2::][::-1]

    if a=='0':
        break

    ans = 0
    
    last = int(a[0])
    tmp = 1
    i = 0
    while tmp:
        if last+tmp==2:
            ans += 1
            i += 1
            try:
                last = int(a[i])
            except:
                break
        else:
            break

    print(ans)