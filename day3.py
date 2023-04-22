# LIST COMPREHENSION #
import functools
import itertools

a = []
for i in range(1, 11):
    a.append(i)
print(a)
# Using list comprehension
b = [i for i in range(1, 11)]
print("Using list comprehension", b)
c = [i for i in range(1, 11) if i % 2 == 0]
print("Number divisible by 2", c)

# DICTIONARY COMPREHENSION #
d = [1, 2, 3]
cd = {}
for i in d:
    cd[i] = i * i * i
print("Cd", cd)

ccd = {i: i * i * i for i in d}
print("Dict comprehension", ccd)

''' Same thing works for tuple and set '''

# Functions
''' Define it using def keyword '''


def add(param_a, param_b=10):
    return param_a + param_b


print("Add", add(3, 4))
print("Default param func", add(3))


def add(param_a):
    return param_a


print("Method Overriding", add(10))     # 10
''' this will call the add function which is written afterwards, because python executes top to bottom '''


def add(param_a, param_b=99):
    return param_a + param_b


print("2nd Method overriding", add(10))


def check_even(param_a):
    if param_a % 2 == 0:
        return True
    return False


print(check_even(10))


# LAMBDA FUNCTIONS

add_l = lambda a, b: a + b
print("Lambda add", add_l(10, 7))

cube_l = lambda a: a*a*a
print("Lambda cube", cube_l(8))
# print("Take input and cube", cube_l(int(input("Enter number: "))))

# MAP, FILTER, REDUCE
''' map is an inbuilt function '''
m1 = [1, 2, 3]
m2 = [1, 4, 9]
s1 = {1, 2, 3, 4}
# map takes a function and an iterable datatype
mp1 = map(lambda x: x*x, m1)
print("mp1", mp1)
print("mp1 type", type(mp1))
print("mp1 list", list(mp1))

st1 = map(lambda x: x*x*x, s1)
print("st1", st1)
print("st1 type", type(st1))
print("st1 set", set(st1))
print("st1 list", list(st1))        # this is [] because it is being used st1 reference us being used by set(st1)

# filter
f1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# f1 = range(1, 10)
ftr1 = filter(lambda i: i % 2 != 0, f1)
print("ftr1", ftr1)
print("ftr1 type", type(ftr1))
print("ftr1 set", set(ftr1))
print("ftr1 list", list(ftr1))


# reduce
''' Gives single value on our iterable data type '''
r1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rd1 = functools.reduce(lambda a, b: a + b, r1, 10)      # third param is accumulator
print("Reduce", rd1)

rd2 = functools.reduce(lambda a, b: a if a > b else b, r1)
print("rd2", rd2)

# EXCEPTION HANDLING


def div(a, b):
    dc = {1: "a", 2: "b"}
    try:
        print("dc of 1: ", dc[1])
        result = a // b
        return result
    except ZeroDivisionError as z:
        print("You can't divide by zero: ", z)
    except KeyError as k:
        print("Please provide correct key: ", k)
    except Exception as e:
        print("Some exception occurred: ", e)
    else:
        print("If no error occurred than this else block gets executed", result)
    finally:
        ''' can be used for cleaning up '''
        print("Finally block executed")


div(3, 1)
print('1' == 1)

# Accumulate
# initializing list
lis = [1, 3, 4, 10, 4]

# printing summation using accumulate()
print("The summation of list using accumulate is :", end="")
print(list(itertools.accumulate(lis, lambda x, y: x + y)))
