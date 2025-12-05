import heapq

for _ in range(int(input())):
    m = int(input())
    n = int(input())

    mz=  tuple(tuple(map(int, input().split())) for _ in range(m))

    # cost, x, y
    heap = [(mz[0][0], 0, 0)]
    dp = [[float('inf')]*(n) for _ in range(m)]
    dp[0][0] = mz[0][0]


    while heap:
        cost, x, y = heapq.heappop(heap)

        if cost > dp[x][y]:
            continue

        for i, j in [(1,0),(-1,0),(0,1),(0,-1)]:
            i += x
            j += y

            if 0<=i<m and 0<=j<n:
                tmp = mz[i][j]+cost
                if tmp < dp[i][j]:
                    dp[i][j] = tmp
                    heapq.heappush( heap,  (tmp, i, j) )
    
    print(dp[-1][-1])