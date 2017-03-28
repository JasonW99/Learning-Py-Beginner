# list ################################################################
classmates = ['Micheal', 'Bob', 'Tracy']
print(classmates)
type(classmates)
len(classmates)

print(classmates[0])
print(classmates[1])
print(classmates[2])
print(classmates[3])

print(classmates[-1])
print(classmates[-2])
print(classmates[-3])
print(classmates[-4])

# add entry at the end
classmates.append('Adam')
print(classmates)

# add entry at specific position
classmates.insert(1, 'Jack')
print(classmates)

# delete the last entry
classmates.pop()
print(classmates)

# delete the entry at the specific position
classmates.pop(1)
print(classmates)

# change the entry at the specific position
classmates[1] = 'Sarah'
print(classmates)

# the entries of a list can be different types
L = ['Apple', 123, True]
print(L)

# the entry of a list can be another list
s = ['python', 'java', ['asp', 'php'], 'scheme']
len(s)
print(s)
print(s[2])

p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']
print(p[1])
print(s[2][1])

# the empty list
L = []
len(L)
print(L)

# tuple ################################################################
# once defined, then cannot be changed

# define the empty tuple
t = ()
print(t)

# define the empty tuple with one element
t = (1,)
print(t)

# define the tuple with one element 1
t = (1)
print(t)

# define the tuple with two element 1 and 2
t = (1, 2)
print(t)

# define a 'changeable' tuple
t = ('a', 'b', ['A', 'B'])
print(t)
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
