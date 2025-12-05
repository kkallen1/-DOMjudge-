def f(a,b,c):
    if a==b==c:
        return a

    return False

d =list(map(str, input().split()))

ans = {'O':0, 'X':0}
a = f(d[0],d[1],d[2])
if a:
    ans[a] += 1
a = f(d[3],d[4],d[5])
if a:
    ans[a] += 1
a = f(d[6],d[7],d[8])
if a:
    ans[a] += 1


a = f(d[0],d[3],d[6])
if a:
    ans[a] += 1
a = f(d[1],d[4],d[7])
if a:
    ans[a] += 1
a = f(d[2],d[5],d[8])
if a:
    ans[a] += 1


a = f(d[0],d[4],d[8])
if a:
    ans[a] += 1
a = f(d[2],d[4],d[6])
if a:
    ans[a] += 1

if ans['O'] == ans['X']:
    print('平手')
elif ans['O'] > ans['X']:
    print('O')
elif ans['O'] < ans['X']:
    print('X')