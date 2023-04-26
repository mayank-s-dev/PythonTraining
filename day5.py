# inheritance

class Parent:
    name = "Parent"

    def __init__(self, name):
        self.name = name

    def intro(self):
        return self.name


class Child(Parent):
    def __init__(self, name, address, mob=8989892222):
        # super().__init__(name)
        Parent.__init__(self, name)
        self.address = address
        self.mob = mob


'''
If child class don't have __init__, then it will look for initializer in its parent class since, child has been 
inherited from Parent
'''

parent = Parent("Main Parent")
obj = Child("Jack", "Pune")
print(obj.name, obj.address)  # you can call Parents attributes
print((obj.intro()))  # you can call Parents method
print(parent.intro())

obj_without_mob = Child("Mayank", "Bhopal")
obj_with_mobile = Child("Rahul", "Delhi", 9090909090)
print(obj_without_mob.intro())
print(obj_with_mobile.intro())

# Polymorphism
'''
Two different class calling the same 'intro' function, so this is polymorphism in python
Similarly, 
one we created object with 3rd(mob) parameter but then we created without parameter,
this is also polymorphism in python
'''


# encapsulation
class Temperature:
    def __init__(self, temp, weather):
        print("eee", temp, weather)
        self.__temp = temp
        self._weather = weather

    def get_temp(self):
        return self.__temp

    def set_temp(self, increase_by):
        self.__temp += increase_by

    def print_private(self):
        return self.__temp


class ChildOfTemp(Temperature):
    # def print_private_wrong_way(self):
    #     return self.__temp + "print_t"

    def print_private_in_child(self):
        return super().print_private()


temperature = Temperature(35, "Hot")
# print(temperature.temp + 5)     # not the proper way to update
temperature.set_temp(5)
print("private attribute", temperature.get_temp())
print("protected attribute direct", temperature._weather)  # can be accessed
# print("private attribute direct", temperature.__temp)       # Error

child_obj = ChildOfTemp(5, "Cold")
# print("childobj", child_obj.print_private_wrong_way())      # this will give error since __temp is private
print("childobj", child_obj.print_private_in_child())  # accessing private of Temperature
'''
restrict access to methods and variables. In encapsulation, code and data are wrapped together within a single unit 
from being modified by accident.
: All operation on attribute should be performed inside class

to update self.temp we should call setter of the class. then only we should update in class

private and protected
: inherit mein PROTECTED can be accessed in child, but private cannot be
: PRIVATE is the most secure access modifier
write __ in front for private variable
_ is protected variable

protected can only be changed where class is accesssible
'''

# ABSTRACTION
'''
If we create abstract class and abstract method, any class which inherits this abstract class is mandatory 
to have that abstract method, see above example

For @abstractmethod to work we need (ABC)
'''
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = a

    def area(self):
        return self.a * self.b


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r


r1 = Rectangle(1, 2)
c1 = Circle(2)


# DECORATORS


def my_decorator(func):
    def inner():
        print("Before function")
        print(func())
        print("After function")
        return "Nooooo"

    return inner


# Before func
# intro(deco):
# 1
# inner1
# After

def intro(func):
    def inner():
        print(func())
        print("inner1")
        return "NONO kI JAGAj"

    return inner


@intro
@my_decorator
def yo():
    return 1


yo()

# Varaible Scope

'''
global scope
local scope
nonlocal scope
'''

a = 10  # global
def print_a():
    a = 20  # local
    print("local a", a)


print_a()
print("global a", a)

b = 10  # global
def print_b():
    # b = b + 10        # this will throw error
    global b
    b = b + 10  # this will throw error since we cannot modify, global directly
    print("Inner", b)


print_b()
print("global b", b)

'''
in below scenario we can't update b, it will throw an error, because inner function will initialise 'b' 
in it's own scope and cannot find it before assignment
'''
def outer():
    b = 10
    def inner():
        # b += 1        # error
        print("b", b)   # this will work, if above line is commented

    inner()
    return inner

inner_func = outer()

# NonLocal
def outer1():
    b = 11

    def inner1():
        nonlocal b;
        b = b + 1
        print("nonlocal", b)

    inner1()

outer1()


class change:

    def __init__(self, x, y, z):
        self.a = x + y + z

x = change(1, 2, 3)
y = getattr(x, 'a')     # y = 6
setattr(x, 'a', y + 1)

print(x.a)

class demo():

        def __str__(self):
            return '__str__ built-in function called'

        def __repr__(self):
            return '__repr__ built-in function called'

s=demo()
print(s)