d = list(map(str, input()))

kk = 'AEIOUaeiou'
idx = {
    x:d.count(x)
    for x in d
    if x in kk
}


if len(idx) == 0:
    print(''.join(d).lower())
elif len(idx) == 1:
    d = [x.upper() if x in kk else x.lower() for x in d]
    print(''.join(d))
else:
    d = [x.swapcase() if x in kk else x.lower() for x in d]
    if d[0] in kk:
        d[0] = d[0].upper()
    if d[-1] in kk:
        d[0] = d[-1].upper()
    print(''.join(d))