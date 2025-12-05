a = int(input())
ans = 0

while pow(2, ans)<=a:
    ans +=1 

print(pow(2, ans-1))