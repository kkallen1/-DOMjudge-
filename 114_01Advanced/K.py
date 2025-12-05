n, k = map(int, input().split())
data = list(int(x) for x in input().split())
q = list(int(x) for x in input().split())

data.sort()
for target in q:
    ans = -1
    l, r = 0, n-1

    while l<=r:
        mid = (l+r) // 2

        if data[mid] == target:
            ans = mid+1
            break

        elif data[mid] > target:
            r = mid-1
        else:
            l = mid+1
    
    print(ans if ans!=-1 else 0)