for _ in range(int(input())):
    d = list(map(str, input().split()))

    stack = []

    for i in d:
        if i.isdigit():
            stack.append(i)
        else:
            b = stack.pop()
            a = stack.pop()
            tmp = int(eval(f"{a}{i}{b}"))
            stack.append(tmp)
    
    print(stack[-1])