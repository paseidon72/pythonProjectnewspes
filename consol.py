
a = input('Введите два слова ').split()

ponchik = a[0]
pirojok = a[1]

s_file = open('test.txt', 'w')
menu = print('!Покупай %(pir)s, выбирай %(pon)s?' %
             {'pir': pirojok.upper(), 'pon': ponchik.capitalize()}, sep='<<>>', file=s_file)


super_menu = print('!Покупай {1}, выбирай {0}?'
                   .format(ponchik.capitalize(), pirojok.upper()), sep='<<>>', file=s_file)


mega_menu = print(F'!Покупай {pirojok.upper()}, выбирай {ponchik.capitalize()}?', sep='<<>>', end='', file=s_file)
s_file.close()
