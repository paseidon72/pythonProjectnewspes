import random
num = input('login ')
pas = ''
for x in range(16):
    pas = pas + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
print('Hello, ', num, 'your password is: ', pas)

