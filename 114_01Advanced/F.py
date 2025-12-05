while True:
    a = bin(int(input()))[2::]
    if a=='0':
        break
    
    print(f"The parity of {a} is {a.count('1')} (mod 2).")