#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# sorted()
sorted([36, 5, -12, 9, -21])

sorted([36, 5, -12, 9, -21], key=abs)

def fn(x):
    return x + 1
sorted([36, 5, -12, 9, -21], key=fn)

# sorted() for str ##########'A'<'Z'<'a'<'z' #########
sorted(['bob', 'about', 'Zoo', 'Credit'])
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)

# sort by name
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(x):
    return x[0]
sorted(L, key=by_name)

def by_score(x):
    return x[1]
sorted(L, key=by_score, reverse=True)