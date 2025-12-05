for _ in range(int(input())):
    n = input()
    if len(n)==5:
        print(3)
        continue

    o = 'one'
    t = 'two'

    ans = [0,0]
    for i in range(3):
        if n[i]==o[i]:
            ans[0]+=1
        if n[i]==t[i]:
            ans[1]+=1
    
    print(1 if ans[0]>ans[1] else 2)