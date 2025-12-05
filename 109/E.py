for _ in range(int(input())):
    n = input()

    dp = set()
    while n not in dp and n!=n[::-1]:
        dp.add(n)
        n = str(int(n) + int(n[::-1]))
    
    if n==n[::-1]:
        print(n)