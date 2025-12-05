for _ in range(int(input())):
    n = int(input())
    a = input()

    ans = set()
    for i in range(n):
        tmp = a[:i:] + a[i+2::]
        if len(tmp)==n-2:
            ans.add(tmp)
    print(len(ans))