a = int(input())

ans = []
for i in range(1, a):
    if a%i==0 and i not in ans:
        ans.append(i)
        ans.append(a//i)

print(sum(ans))