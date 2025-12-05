a = list(x for x in input())

flag = 1
stack = [] # {

max_deep = 0
deep = 0
for i in a:
    if i=='}' and not stack:
        flag = 0
        break
    
    if i=='{':
        stack.append(i)
        deep += 1
    elif i=='}':
        stack.pop()

        if deep > max_deep:
            max_deep = deep
        deep -= 1

if stack or not flag:
    print(-1)
else:
    print(max_deep)