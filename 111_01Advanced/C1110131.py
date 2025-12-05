n = int(input())
for _ in range(n):
    a = int(input())

    if a%4==0 and (a%100!=0 or a%400==0):
        print("a leap year")
    else:
        print("a normal year")