import pyqrcode
import random

r = lambda: random.randint(0,255)

text = input('Введите текст или вставьте ссылку: ')
url = pyqrcode.create(str(text))
url.svg('qr.svg', scale=2, background='#%02X%02X%02X' % (r(), r(), r()), module_color='#%02X%02X%02X' % (r(),r(),r()))
print(url.terminal(quiet_zone=1))