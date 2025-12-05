while True:
    try:
        data = list(int(x) for x in input())

        ans = 0
        tmp = 0
        for i in range(1, len(data) ):
            if not data[i]<data[i-1]:
                tmp += 1
            else:
                if ans<tmp:
                    ans = tmp
                    tmp = 0
        
        if ans<tmp:
            ans = tmp

        print(ans+1)

    except EOFError:
        break