# -*- coding: utf-8 -*-

# dict ####################################################
d = {'Micheal': 95, 'Bob': 75, 'Tracy': 85}
print(d['Micheal'])

# add element in a dict element=key+value
d['Adam'] = 67
print(d)
print(d['Adam'])

d['Jack'] = 90
print(d['Jack'])
d['Jack'] = 88
print(d['Jack'])

# get an non-exist element in a dict
print(d['Tomas'])
print('Tomas' in d)

print(d.get('Tomas'))  # return None value
print(d.get('Tomas', -123)) # return defined value

# remove an element from the dict pop(key)
d.pop('Bob')
print(d)
len(d)

# the key of a dict cannot be a list
key = [1, 2, 3]
type(key)
d[key] = 56

# set ####################################################
# set contains only key, but no corresponding value
keys = [1, 2, 3]
s = set(keys)
print(s)

keys = [1, 1, 2, 2, 3, 3, 3]
s = set(keys)
print(s)

# add keys into a set
s.add('hehe')
print(s)

s.add(3)
print(s)

# remove keys from a set
s.remove(3)
print(s)

# sets algorithm
s1 = set([1, 2, 3])
s2 = set([1, 2, 4])
print(s1 & s2)
print(s1 | s2)

# the key of a set cannot be a list
s.add([3, 6]) # list
s.add((3, 6))
print(s)      # tuple
s.add((3, [1, 2]))# tuple

# changeable(list) and unchangeable(str & set & dict)
a = ['c', 'b', 'a']
print(a)
a.sort()
print(a)

a = 'abc'
a.replace('a', 'A')
print(a)




