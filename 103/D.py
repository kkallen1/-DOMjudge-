for _ in range(int(input())):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    print(len(set(a[1::])&set(b[1::])))