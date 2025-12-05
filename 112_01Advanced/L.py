while True:
    n = input()
    if n=='0':
        break

    while len(n)!=1:
        n = str(sum( [int(x) for x in n] ))
    
    print(n)