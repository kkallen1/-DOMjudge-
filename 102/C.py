import itertools

for _ in range(int(input())):
    tmp = list(eval(input()))
    a = tmp[0]
    b = tmp[1]

    ans = [a|b, a&b, a-b, (a|b) - (a&b)]
    
    ans = [x if x else 'N' for x in ans]
    print(*ans, sep=', ')