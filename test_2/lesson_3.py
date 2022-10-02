
n = int(input())
h = n // 3600
h = h % 24
n = n % 3600
min_m = n % 3600
hv = min_m // 60
min_d = hv // 10
min_e = hv % 10
sec = n % 60
sec_d = sec // 10
sec_e = sec % 10
print(h, ":", min_d, min_e, ":", sec_d, sec_e, sep="")
