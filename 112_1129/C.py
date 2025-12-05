a = int(input())+1911
if a%4==0 and (a%100!=0 or a%400==0):
    print(True)
else:
    print(False)