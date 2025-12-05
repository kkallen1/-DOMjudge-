while True:
    try:
        s,d=map(int,input().split())
        end=1
        while d-(s+end+10**12)*(end-s+1+10**12)/2>0:
            end+=10**12
        while d-(s+end+10**10)*(end-s+1+10**10)/2>0:
            end+=10**10
        while d-(s+end+10**9)*(end-s+1+10**9)/2>0:
            end+=10**9
        while d-(s+end+10**8)*(end-s+1+10**8)/2>0:
            end+=10**8
        while d-(s+end+10**7)*(end-s+1+10**7)/2>0:
            end+=10**7
        while d-(s+end+10**6)*(end-s+1+10**6)/2>0:
            end+=10**6
        while d-(s+end+10**5)*(end-s+1+10**5)/2>0:
            end+=10**5
        while d-(s+end)*(end-s+1)/2>0:
            end+=1
        print(end)
    except:
        break

'''
while True:
    try:
        s,d=map(int,input().split())
        end=1
        while d-(s+end)*(end-s+1)/2>0:
            end+=1
        print(end)
    except:
        break
'''
