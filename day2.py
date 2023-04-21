print("day2")

# DATA TYPE OPERATIONS #

''' types of data int float string tuple list set and dictionary '''

a = 20
a = a + 1  # 21
a += 1  # 22
print("a", a)

# *swap
a = 20
b = 40
a, b = b, a

''' 
There is not data type as character in python, single character is also a string, string is immutable
just like tuple so string can't be modified
'''
name = 'a'  # datatype string
print('datatype of name', type(name))
name = "Jake John Mike"
# name[0] = "u"     # throw error, trying to change string
print("First Character", name[0])
print("Last character", name[-1])
''' no need to know the length of string in python, we can also access last element in list in such a way '''

''' split will split the string on specified character, by default it will split by space '''
print("split by default", name.split())
print("split by space", name.split(" "))
print("split by o", name.split("o"))

# *there are other list operations as well

# LIST OPERATIONS
l = [1, 2, 3]
l.append(4)
print("l appended", l)

l.insert(1, 'a')
print("a appended to list", l)

l.remove("a")
print("a removed from the list")

# l.remove("f")   # will throw error since f is not in the list, before calling remove call 'in'

print("in-operation", 'f' in l)

# l.append([5, 6, 7])
# print("appended list to a list", l)  # appended list to a list [1, 2, 3, 4, [5, 6, 7]]

l.extend((5, 6, 7))
print("appending list to a list correct way", l)

# TUPLE OPERATIONS
t = (1, 2)
# t[0] = 3      # will throw error, cannot modify tuple

print("Count tuple", t.count(4))  # count returns, count of any element in the list
print("Index tuple", t.index(1))  # index returns, index at which the given element is present

# DICTIONARY OPERATIONS

d = {1: 'a', 2: 'b'}
print("Access dictionary element", d[1])  # a
print("Access dictionary element using get method", d.get(1))  # a

# * accessing not present element in dictionary
# print("Not present", d[3])      # throw error
print("Not Present", d.get(3))      # None
print("Not present default value:", d.get(3, 'not available'))

print("All keys", d.keys())
print("All values", d.values())
print("all items", d.items())       # return tuples

# SET OPERATIONS
s = set([1, 2, 3, 3, 4])
s.add(5)
print("Added element to set", s)
s.add(1)
print("Added already present element in set", s)

# there are other set opearations as well

# CONDITIONS #

if 2 == 2:
    print("2 is equal to 2")
    print("This line comes in scope of above if statement")

print("This line is not in scope if above if statement")

if 2 == 3:
    print("2 is equal to 2")
elif 3 == 3:
    print("3 is equal to 3")
elif 1 == 1:
    print("1 is equal to 1")
else:
    print("we are in else statement")

# LOOPS #

# for, while
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print("Fruit", fruit)
    print("Upper Fruit", fruit.upper())
else:
    print("Fruits are finished in list")

# Loop on tuple
fruits = ('apple', 'banana', 'cherry')
for fruit in fruits:
    print("tuple Fruit", fruit)
    print("tuple upper Fruit", fruit.upper())
else:
    print("Fruits are finished in tuple")

# range()
for i in range(1, 10):
    # default increment by 1
    print(i, end=" ")

print("\n")
# range doesn't include the last element, default increment by 1
for i in range(1, 10, 2):
    # increment by 2
    print(i, end=" ")


# while

# while i < 5:
#     print(i)
# when python detects infinite loop it doesn't run the program
print("\n")
i = 1
while i < 5:
    i += 1
    if i == 2:
        i += 1
        continue
    print(i)
    if i == 3:
        print("3 arrived")
        pass
        # pass : do nothing
        # continue: skip that iteration in the loop
else:
    print("While loop ended")

marks = 23
if 80 <= marks <= 100:
    print("Grade", "A")
elif 60 <= marks <= 79:
    print("Grade", "B")
elif 40 <= marks <= 59:
    print("Grade", "C")
elif 0 <= marks <= 39:
    print("Grade", "D")

for i in range(0, 31):
    if i % 2 == 0:
        print("Number", i)

x = ['ab', 'cd']

x = ['1', 'a', '1a', 'b1', '$']

newList = [i.isdigit() for i in x]      # list comprehension
'''
above line works like this
newList = []
for i in x:
    newList.append(i.isdigit())
'''
print(1 for i in x)