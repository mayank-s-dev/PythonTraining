# Non Local Scope

a = 1


def outer(a=2):
    def inner():
        # global a
        print("Inner of function", a)

    inner()


print("Outside of function", a)
outer()

a = 1

# -----------------

a1 = 3


def outer1(a1=4):
    def inner1():
        global a1
        print("Inner of function:::", a1)

    inner1()


print("Outside of function:::", a1)
outer1()

# -----------------

a3 = 3


def outer3(a3=4):
    def inner3():
        # a3 += 10      # this line will run into error, it will work when we add
        nonlocal a3  # this nonlocal will point to outer function a3
        a3 += 10
        print("Inner of function^^^", a3)

    inner3()


print("Outside of function^^^", a3)
outer3()

# -----------------

# MODULES AND PACKAGES
'''
Any file with .py extension is a module
and packages is a directory which contain those files
So the difference b/w directory and package is, to make directory a package we need to create an init file
'''

# Using functions from MyPackage
from MyPackage import calculator, bank

help(calculator.add)  # help doesn't need print, it prints automatically
# help module can give help about anything
print("Calculator add", calculator.add(2, 8))

help(calculator.subtract)
print(calculator.subtract.__annotations__)
print("Calculator sub", calculator.subtract(2, 8))

print(calculator.multiple.__annotations__)
print("Calculator mul", calculator.multiple(2, 8))

# OS MODULE AND PATH MODULE
'''
os is a package which contains multiple modules
: running things related to operating system, traversing thorough directories to get files
'''

import os

# current working directory
print("os name", os.name)
print("os current directory", os.curdir)
print("os.listdir", os.listdir())  # list files/folders in current directory

print("Bank current directory", bank.get_current_directory())

print("os.path.abspath", os.path.abspath("assignment_video_2.py"))

# print("os.environ", os.environ)       # commented because list is big

print("os.get cwd", os.getcwd())

os.chdir('./MyPackage')  # change directory
print("os.get cwd after changing dir", os.getcwd())

os.mkdir("InnerPackage")  # create new dir
print("Created inner package", os.listdir())
os.rmdir("InnerPackage")  # remove dir
print("Removed inner package", os.listdir())

# create directory within a directory

''' first create the base directory '''
os.mkdir("InnerPackage")  # create new dir
os.mkdir("InnerPackage/Package1")  # this will work only if InnerPackage exist in current directory
# os.rmdir("InnerPackage")  # removing it, but will give error because, The directory is not empty: 'InnerPackage'

''' removing one by one for now, removing what I created to test    '''
os.rmdir("InnerPackage/Package1")
os.rmdir("InnerPackage")

''' 
if you don't want to create base directory do this
This will create InnerPackage first then inside of it will create Package1
'''
os.makedirs("InnerPackage/Package1")
# removing what I created to test
os.rmdir("InnerPackage/Package1")
os.rmdir("InnerPackage")

# help(os)      # commenting for now, taking more space in console

# PATH MODULE
os.chdir('../')  # change directory

print("Path module:os.path.curdir: ", os.path.curdir)
print("os.path.abspath: ", os.path.abspath("./"))
print("rel path", os.path.relpath('C:/Users/mayan/PycharmProjects/Day1Python/MyPackage/bank.py'))

print("basename: ", os.path.basename("C:/Users/mayan/PycharmProjects/Day1Python/MyPackage/bank.py"))
# the above line basically prints file name at the end of the path

# PIP
''' python installer package '''
import pytest

print(pytest)

### QUIZ

class A():
    def disp(self):
        print("A disp()")

class B(A):
    pass

obj = B()

obj.disp()

# ques 2
class Demo:
    def __init__(self):
        self.x = 1
    def change(self):
        self.x = 10
class Demo_derived(Demo):
    def change(self):
        self.x = self.x + 1
        return self.x
def main():
    obj = Demo_derived()
    print(obj.change())

main()