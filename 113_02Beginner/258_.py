import itertools

a = input()

data = list(itertools.permutations(a, len(a)))

for i in range(len(data)):
    data[i] = int("".join(data[i]))

data = list(set(data))
data.sort(reverse=True)
data.remove(int(a))

print(*data, sep="\n")