
A = int(input())
B = int(input())
C = int(input())
D = int(input())
cost1 = A * 100 + B
cost2 = C * 100 + D
total = cost1 + cost2
print(total // 100, 'грн', total % 100, 'коп')

