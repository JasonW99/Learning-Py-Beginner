#  1. define a function and use map to assign value pairs
def normalize(name):
    return name.capitalize()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

#  2. use 'input()' to collect information
name = input('please enter your name: ')
print('Hello,', name)

# 3. control flow using if else
a = 100
if a >= 0:
    print(a)
else:
    print(-a)



exit()