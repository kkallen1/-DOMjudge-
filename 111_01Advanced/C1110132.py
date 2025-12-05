a = int(input())
for i in range(1, a+1):
    y = int(input())
    if y%4==0 and (y%100!=0 or y%400==0):
        print(f"Case {i}: a leap year")
    else:
        print(f"Case {i}: a normal year")