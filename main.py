
#ponchik = 'пончик'
#pirojok = 'пирожок'

#s_file = open('test.txt', 'w')
#menu = print('!Покупай %(pir)s, выбирай %(pon)s?' %
      #{'pir': pirojok.capitalize(), 'pon': ponchik.upper()}, sep='<<>>', end='', file=s_file)

#s_file.close()

a = input('Введите два слова ').split()

ponchik = a[0]
pirojok = a[1]

print(ponchik)
print(pirojok)

print(type(a))
print(a)



