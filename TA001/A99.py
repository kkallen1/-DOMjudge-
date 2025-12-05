import datetime

for _ in range(int(input())):
    m,d = map(int, input().split())
    now = datetime.date(2021,m,d)

    week = [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday'
    ]

    print(week[now.weekday()])