# read from file
"""
# you can access a file with absolute path also
file = open("sample.txt")       # file opened in read mode, you cannot use file.write("newdata")
print(file.read())     # argument is no of characters you want to read
print(file.readline())      # read and readline will read from where the cursor was present,
                            # it will only read oneline at a time and the no of characters were passed

file.seek(2)        # seek will move the cursor back to the front of line
print((file.readline()))
file.close()
"""

# Assignment: read for differences b/w read and readline

# read, write and append

# read - r
# write - w
# append - a
# w+ - read and write (this will truncate the data present in the file)
# r+ - read and write (this will not truncate the existing data, this kind of work file appending)

file = open("sample.txt", "w+")
print(file.read())
print(file.writable())  # True
file.write("AAAAAAAAAAa")
file.seek(0)
print(file.readline())
file.close()

''' r+ and append are same, the difference is when you use r+ you need to bring the pointer 
to initial position using seek'''

# open a file which don't exist, if read mode it will give error and in write mode it will create
# file = open("hello.txt", "r")       # gives error

file = open("hello.txt", "w")  # creates new file if it doesn't exist
file.close()

# why file.close is imp?
# - it fries up system resources
# - and if multiple resources uses the same file, it will create ambiguity

'''
for i in range(100):
    file = open("Hello.txt", "r+")
    file.write("!")
    file.close()
'''

# context manager
with open("sample.txt") as i:
    print("with", i.read())
print("File automatically closes after indentation")

# when the indentation of 'with' ends, it automatically closes the file

# Assignment: Create a file, read data, manipulate data


# OOP #

# class and objects:

'''
collection of objects
'''


class Animal:
    """
        - class has attributes and methods
        attributes: name, age
        methods: fly, walk, swim, intro
        - types of methods in class: static method, instance method and class method
            : instance method: intro is an instance method, because it accesses instance of class(self)
            : static method: which doesn't have self as parameter
   """

    address = "Pune"  # address is a default attribute of our class

    def __init__(self, name="animal", age=0):
        # we can use any work apart from 'self'
        # 'self' points to our class itself
        # overloading doesn't work with __init__
        self.name = name
        self.age = age

    def intro(self):  # instance method
        print("My name is:", self.name)

    def fly(self):  # instance method
        print("I can fly")

    @staticmethod
    def walk():
        print("I can walk")


dog = Animal("JackTheDog", 5)
cat = Animal("Kitty", 3)
unknown = Animal()

# print("DOG:", dog.name, dog.age, dog.address, dog.intro())
dog.intro()
cat.intro()
unknown.intro()
Animal.walk()  # calling static method
# Animal.intro()      # cannot be called, since it's an instance method

# INHERITANCE
'''
Inheritance is parent child relationship
'''


class Person(Animal):       # to inherit multiple classes Person(Animal, OtherClass)
    """
    # if you want to parent class constructor explicitly, we do that when we inherit multiple class
    def __init__(self, name, age):
        super().__init__(name, age)
    """
    def person_name(self):
        print("Person", self.name)


jack = Person("Jack", 25)
jack.intro()
jack.person_name()

# ABSTRACTION
'''
- we don't care what's happening inside, implementation details are hidden
- functions are defined outside of our class are functions, and which are defined inside the class are methods
'''

# s=["pune", "mumbai", "delhi"]

# print([(w.upper(), len(w)) for w in s])

# str = input("Enter your input: ");
# print(str)

def mk(x):
    def mk1():
        print("Decorated")
        x()
    return mk1

def mk2():
    print("Ordinary")

p = mk(mk2)
print(p)
p()



g = (i for i in range(5))
print(type(g))

names1 = ['Alice', 'Bear', 'Charlton', 'Daman']
names2 = names1
names3 = names1[:]
names2[0] = 'Alice'
names3[1] = 'Bob'
sum = 0

for ls in (names1, names2, names3):
    if ls[0] == 'Alice':
        sum += 1
    if ls[1] == 'Bob':
        sum += 10

print(sum)