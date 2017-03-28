# 1. integer
a = 8
print(type(a))
print(a/3)

# 2. float
b = 1.0
print(type(b))

# 3. str and escape codes
print('I\'m \"ok\"!')
print('I\'m learning \nPython')
print('\\\n\\')
print('\\\t\\') # '\t' means TAB
print(r'\\\t\\') # command within r'' will be no escape
print('''line1
line2
line3''') # change several lines
print(r'''line1
line2
///n
line3''')

# 4. Boolean
print(True or True)
print(True or False)
print(False or False)
print(5 > 3 or 1 > 3)

print(not True)
print(not False)
print(not 1 > 2)

if a > 18:
    print('adult')
else:
    print('teenager')

# 5. None is not zero

# 6. Variable
a = 1
t_007 = 'T007'
Answer = True
a = 123
print(a)
a = 'ABC'
print(a)

x = 10
x = x + 2

y = 'ABC' #1.create a str 'ABC' 2.create a variable x and point its value to 'ABC'
print(y)
z = y
print(z)
y = 'XYZ'
print(y)
print(z)

# 7. constant(use upper case to define constant)
PI = 3.14159265359
print(PI)

# 8. Division
print(10 / 3)
print(6 / 3)
print(8 / 3)
print(8 // 3)
print(10 % 3)

