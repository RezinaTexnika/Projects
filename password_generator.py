import random
import time

a = 'qwertyuiopasdfghjklzxcvbnm'
b = 'QWERTYUIOPASDFGHJKLZXCVBNM'
c = '0123456789'
d = '[]{}()*"/,._-!?+<>=@#$%^&|'

all_symbol = a + b + c + d
length = 12
password = ''.join(random.sample(all_symbol, length))
print('Идет генерация пароля...')
time.sleep(3)
print('Ваш пароль готов:')
print(password)
input()
