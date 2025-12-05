D = {
    '-----': '0',
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',
}

for _ in range(int(input())):
    d = list(map(str, input().split()))

    ans = []
    for i in d:
        ans.append(D[i])
    
    print(''.join(ans))