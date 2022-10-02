
n = int(input('enter n: '))
dig1 = n // 100
n = n - dig1 * 100
dig2 = n // 10
dig3 = n - dig2 * 10
print(dig1 + dig2 + dig3)

