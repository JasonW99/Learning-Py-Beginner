# ASCII English coding
# Unicode all language coding
# UTF-8 all language coding but save space for English words

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

ord('A')
ord('中')
chr(66)
chr(25991)
print('\u4e2d\u6587')


x = 'ABC' # str
y = b'ABC' # bytes

'ABC'.encode('ascii')
'中文'.encode('utf-8')
'中文'.encode('ascii')

b'ABC'.decode('ascii')
b'ABC'.decode('utf-8')
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

len('ABC')
len('中文')

len(b'ABC')
len(b'\xe4\xb8\xad\xe6\x96\x87')
len('中文'.encode('utf-8'))


'''
%d is for integer
%f is for float
%s is for string
%x is for hexadecimal integer
'''
print('hello, %s' % 'world')
print('Hi, %s, you have $%d' % ('Micheal', 1000))

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
print('Age: %s. Gender: %s' % (25, True))
print('growth rate is %.2f%%' % 24.3)