while True:
    a = int(input())
    if a==0:
        break

    if a%4==0 and (a%100!=0 or a%400==0):
        print('a leap year')
    else:
        print('a normal year')