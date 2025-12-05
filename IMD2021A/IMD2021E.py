while True:
    n = int(input())

    if n == 0:
        break

    print(f"The parity of {bin(n)[2::]} is {bin(n)[2::].count('1')} (mod 2).")