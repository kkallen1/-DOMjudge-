d = list(map(str, input().split()))

stack = []
num = []
for i in d:
    if i.isdigit():
        num.append(i)
    else:
        if len(num)>1:
            b = num.pop()
            a = num.pop()

            num.append(int(eval(f"{a}{i}{b}")))
print(num[0])