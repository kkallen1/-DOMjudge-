for _ in range(int(input())):
    a, b = map(int, input().split('/'))

    if (a==1 and 21<=b<=31) or (a==2 and 1<=b<=19):
        print("Aquarius")
    elif (a==2 and 20<=b<=29) or (a==3 and 1<=b<=20):
        print("Pisces")
    elif (a==3 and 21<=b<=31) or (a==4 and 1<=b<=20):
        print("Aries")
    elif (a==4 and 21<=b<=30) or (a==5 and 1<=b<=21):
        print("Taurus")
    elif (a==5 and 22<=b<=31) or (a==6 and 1<=b<=21):
        print("Gemini")
    elif (a==6 and 22<=b<=30) or (a==7 and 1<=b<=22):
        print("Cancer")
    elif (a==7 and 23<=b<=31) or (a==8 and 1<=b<=21):
        print("Leo")
    elif (a==8 and 22<=b<=31) or (a==9 and 1<=b<=23):
        print("Virgo")
    elif (a==9 and 24<=b<=30) or (a==10 and 1<=b<=23):
        print("Libra")
    elif (a==10 and 24<=b<=31) or (a==11 and 1<=b<=22):
        print("Scorpio")
    elif (a==11 and 23<=b<=30) or (a==12 and 1<=b<=22):
        print("Sagittarius")
    elif (a==12 and 23<=b<=31) or (a==1 and 1<=b<=20):
        print("Capricorn")