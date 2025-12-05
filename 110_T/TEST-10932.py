import datetime

for _ in range(int(input())):
    n = int(input())

    date = datetime.date(1970, 1, 1)
    date += datetime.timedelta(days=n)
    print(date)