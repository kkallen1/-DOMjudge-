import decimal

for _ in range(int(input())):
    ans = decimal.Decimal(input())
    ans = ans.quantize(
        decimal.Decimal('0.01'),
        rounding=decimal.ROUND_HALF_UP
    )

    if ans == -0.00:
        print('0.00')
    else:
        print(ans)