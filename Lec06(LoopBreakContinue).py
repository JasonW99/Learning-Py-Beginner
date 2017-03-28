# -*- coding: utf-8 -*-
# for loop
names = ['Micheal', 'Bob', 'Tracy']
for name in names:
    print(name)

Sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    Sum = Sum + x
print(Sum)

list(range(11))
sum(range(11))

Sum = 0
for x in range(101):
    Sum = Sum + x
print(Sum)

# Fibonacci series ##################################
def fib(n):
    if n <= 2:
        return 1
    lead1 = 1
    lead2 = 1
    for i in range(3, n + 1):
        current = lead1 + lead2
        lead2 = lead1
        lead1 = current
    return current

fib(7)

def fib_series(n):
    if n <= 1:
        return [1] * n
    result = [1] * n
    for i in range(2, n):
        result[i] = result[i-2] + result[i-1]
    return result

fib_series(7)

#######################################################

# while loop
Sum = 0
n = 99
while n > 0:
    Sum = Sum + n
    n = n - 2
print(Sum)

# break
n = 1
while n <= 100:
    print(n)
    n = n + 1
print('End')

n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print('End')

# continue
n = 0
while n <= 10:
    print(n)
    n = n + 1

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)


