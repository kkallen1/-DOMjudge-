import datetime

tmp = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday', 'Sunday']
for _ in range(int(input())):
    a, b = map(int, input().split())

    now = datetime.date(2023, a, b)

    print(tmp[now.weekday()])