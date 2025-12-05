D = {
    "I":1,
    "IV":4,
    "V":5,
    "IX":9,
    "X":10,
    "XL":40,
    "L":50,
    "XC":90,
    "C":100,
    "CD":400,
    "D":500,
    "CM":900,
    "M":1000,
}

for _ in range(int(input())):
    n = list(map(str, input()))

    ans = 0
    last = 0
    while n:
        now = D[n.pop()]
        if now>=last:
            ans += now
        else:
            ans -= now
        last = now
    print(ans)