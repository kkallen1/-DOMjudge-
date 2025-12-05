import itertools

a = input()

tmp = list(itertools.permutations(a, len(a)))

data = []
for i in tmp:
    data.append(int("".join(i)))

ans = set()
for i in data:
    if i%11 == 0:
        ans.add(i)

print(len(ans))