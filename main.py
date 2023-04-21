# Python Training

# print("You can do it")
""" sec-1
Duck typing is a concept related to dynamic typing, where the type or the class of an object
is less important than the methods it defines. When you use duck typing, you do not check types at all. Instead,
you check for the presence of a given method or attribute.
Duck-typing emphasis what the object can really do, rather than what the object is.
"""

# """ there are called docstrings '''
# There is no need to assign datatype to a variable, python automatically detects


""" sec-2
a = 5
b = "Just believe, have faith"
print(b)
print(a, b)
print(a, " ", b)
print(a, "\n", b)

Assignment: 
1. How to type cast
: int(), str(), float()
2. How to take input from user
: Python take all inputs as string, then you need to typecast
inp = input('STATEMENT\n')
print(inp, type(inp))
"""

""" sec-3
# DATATYPES
a = 5
b = "Come On"
c = 5.0
d = True  # T should be capital in boolean
f1 = None  # None is like null, no value
print(type(a), type(b), type(c), type(d), type(f1))
# <class 'int'> <class 'str'> <class 'float'> <class 'bool'> <class 'NoneType'>

# list are somewhat similar to array, but list can store multiple datatype in same list
e = [a, b, c, d, f1, 1]
print(e)  # [5, 'Come On', 5.0, True, None, 1]
e[0] = 1
print(e)  # [1, 'Come On', 5.0, True, None, 1]

# Python executes code from top to bottom and stop when there is an error at any point

# tuple: are similar to list, but it can't be modified
f = (5, 5)
print(f, type(f))  # (5, 5) <class 'tuple'>
# f[0] = 1  # error: can't modify a tuple
# typecasting tuple to list
newTuple = (1, 2)
newList = list(newTuple)
print("newTuple:", newTuple)
print("newList:", newList)

# set: it only stores unique values and SORTS them, remove if there are any duplicate
g = {5, 5, "Hello", 1, "a"}
print("set:", g, type(g))  # set: {1, 'Hello', 'a', 5} <class 'set'>

# dictionary: it stores key-value pairs
h = {1: "Jan", 2: "Feb", 3: "Mar", "four": "April", 1: "January"}  # duplicate key be overwritten
print("dictionary:", h, type(h))  # dictionary: {1: 'January', 2: 'Feb', 3: 'Mar', 'four': 'April'} <class 'dict'>
print("dictionary access:", h[1], h["four"])
"""

# OPERATORS: (Arithmetic, Relational, Logical
# Arithmetic
print("Arithmetic")
a = 5 + 5
print("a:", a, type(a))  # a: 10 <class 'int'>

b = 5 + 5.0
print("b:", b, type(b))  # b: 10.0 <class 'float'>

c = 5 * 8 + 10 - 7
print("c:", c, type(c))  # c: 43 <class 'int'>

d = 25 / 5
print("d:", d, type(d))  # d: 5.0 <class 'float'>

e = 26 // 5
print("e:", e, type(e))  # e: 5 <class 'int'>

# Relational
# ==
# >
# <
# >=
# <=
# !=
# == is
# ! not

c = 3
d = 4
print(c is d)
print(c is not d)
print("c:", not c)
print(c or d)  # returns 3 # or is looking for one true value
print(c and d)  # returns 4 # and is looking for two true value

e = True
f = False
print(e is f)
print(e is not f)
print(not e)

g = None
h = 2
print("g")
print(g is h)
print(g is not h)
print(not g)

print("Logical")
print(g or h)
print(g and h)

a1 = 1
b1 = False
print("a1:b")
print(a1 or b1)
print(a1 and b1)

# operator precedence
print('pp', a1 or b1 and b1)
# "and" precedes "or"

print('ll', type(1 and False))
print(not a)
a = 10
print(not a)
# print(!a)  # doesn't work
