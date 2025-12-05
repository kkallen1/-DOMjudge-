d =list(map(str, input().split()))

stack = []
ans = []
for now in d:
    if now=='(':
        stack.append(now)
    elif now == ')':
        tmp = []
        while stack[-1] != '(':
            ans.append(stack.pop())
        stack.pop()
    elif now in '*/':
        while stack and stack[-1] != '(' and stack[-1] in '*/':
            ans.append(stack.pop())
        stack.append(now)
    elif now in '+-*/':
        while stack and stack[-1] != '(' and stack[-1] in '+-*/':
            ans.append(stack.pop())
        stack.append(now)
    else:
        ans.append(now)
while stack:
    ans.append(stack.pop())
print(*ans)