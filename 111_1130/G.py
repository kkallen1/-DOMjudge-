for _ in range(int(input())):
    a = input()

    ans = []
    stack = []
    num = []
    for i in a:
        if i.isdigit():
            num.append(i)
        else:
            if num:
                num = int(''.join(num))
                ans.append( ''.join(stack)*num )
                stack = []
                num = []

            stack.append(i)
    if num:
        num = int(''.join(num))
        ans.append( ''.join(stack)*num )
    print(*ans, sep="")