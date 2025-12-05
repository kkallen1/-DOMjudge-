while True:
    try:
        a = int(input())

        ans = []
        for i in range(1, a//2+1):
            if a%i==0:
                if i not in ans:
                    ans.append(i)
                if a//i not in ans:
                    ans.append(a//i)
        print(sum(ans))
    except EOFError:
        break