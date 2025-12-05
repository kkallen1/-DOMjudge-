import heapq

while True:
    n = int(input())
    if n==0:
        break

    d = list(map(int, input().split()))
    heapq.heapify(d)

    ans = 0
    while len(d)>1:
        a = heapq.heappop(d)
        b = heapq.heappop(d)
        tmp = a+b
        
        ans += tmp
        heapq.heappush(d, tmp)

    print(ans)