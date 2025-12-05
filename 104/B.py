import itertools

n = int(input())
currect = list(map(int, input().split(',')))

for _ in range(n):
    d = list(map(int, input().split(',')))

    d = list(itertools.combinations(d, 5))

    ans = [0,0,0,0,0,0]
    for i in d:
        tmp = 0
        for j in i:
            if j in currect:
                tmp += 1
        
        ans[tmp]+=1
    
    print(*ans[2::], sep=",")