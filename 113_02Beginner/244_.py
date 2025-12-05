a, b = map(str, input().split(', '))

a = int(a, 3)
b = int(b, 6)
# print(a, b)

a, b = a+b, 0
# print(a, b)
# print()
ans = []
while a != 0:
    b = a%5
    a = a//5
    # print(a, b)
    ans.append(b)

print(*ans[::-1], sep="")