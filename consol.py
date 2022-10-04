
a = int(input('enter first number: '))
b = int(input('enter second number: '))
k = (a % b) // a * b
l = (b % a) // b * a
n = (a // b) * (b // a) *a
print(k + l + n)


