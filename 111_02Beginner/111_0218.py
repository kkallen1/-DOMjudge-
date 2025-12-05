a = list(int(x) for x in input())

count = [0, 0]

now = a[0]
now_count = 0
for i in a:
    # print(i, now, now_count)
    if now == i:
        now_count += 1
    else:
        count[now] = max(count[now], now_count)

        now = 0 if now else 1
        now_count = 1
count[now] = max(count[now], now_count)

# print(count)
print(abs(count[0] - count[1]))