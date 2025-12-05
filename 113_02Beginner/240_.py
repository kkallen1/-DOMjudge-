a = [x for x in input()]
if (any(x in a for x in [chr(y) for y in range(65, 90+1)]) and
    any(x in a for x in [chr(y) for y in range(97, 122+1)]) and
    any(x in a for x in [chr(y) for y in range(48, 57+1)])
):
    flag = 1
    big = 0
    for i in a:
        if 65<=ord(i)<=90:
            big = 1
        if 97<=ord(i)<=122 and big:
            flag = 0
            break
    print(flag)
else:
    print(0)