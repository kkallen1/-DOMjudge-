a = input()

stack = []
flag = 1

for i in a:
    if i in '([{':
        stack.append(i)
    else:
        if stack:
            if i == ')' and '(' in stack:
                stack.remove('(')
                continue
            elif i == ']' and '[' in stack:
                stack.remove('[')
                continue
            elif i == '}' and '{' in stack:
                stack.remove('{')
                continue
            else:
                flag = 0
                break
        else:
            flag = 0
            break
if stack or not flag:
    print(0)
else:
    print(1)