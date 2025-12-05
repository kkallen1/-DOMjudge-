a=  input()

ans = [0,0,0,0,0,0]
D = { '!', '@', '#', '$', 'ˆ', '&', '*', '(', ')', '?', '”', ':', '{', '}', '|', '<', '>' }
if len(a)>=8:
    ans[1]= 1

for i in a:
    if i.isdigit():
        ans[2] = 1
    elif i in D:
        ans[5] = 1
    elif i == i.upper():
        ans[3] = 1
    elif i == i.lower():
        ans[4] = 1
print(sum(ans))