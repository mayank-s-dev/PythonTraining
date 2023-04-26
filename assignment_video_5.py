# Create animal base class with attribute and related methods then create sub concrete subclass using animal eg of
# subclass: cow, horse, dog
import functools


class Animal:
    def __init__(self, name, animal_type):
        self.name = name
        self.type = animal_type

    def get_type(self):
        return self.type

    def get_age(self):
        return self.age


class Cow(Animal):
    def __init__(self, name):
        super().__init__(name, "Cow")


cow_1 = Cow("Rani")
print(cow_1.name, cow_1.type)


class Horse(Animal):
    def __init__(self, name):
        super().__init__(name, "Horse")


horse_1 = Horse("Stalin")
print(horse_1.name, horse_1.type)


# Create arithmetics class to calculate avg, mean, mode and standard deviation

class Ari:
    def __init__(self, input_number):
        self.input = input_number

    def check_list(self):
        if type(self.input) is not list:
            return "Please input list"

    def mean(self):
        self.check_list()

        if type(self.input) is not list:
            return "Please input list"

        sum_of_element = functools.reduce(lambda a, b: a + b, self.input, 0)
        return sum_of_element / len(self.input)

    def median(self):
        self.check_list()
        input_length = len(self.input)

        if input_length % 2 == 0:
            return self.input[int(input_length / 2) + 1]
        else:
            return self.input[int(input_length / 2)]

    def mode(self):
        self.check_list()
        sorted_input = [1, 1, 2, 2, 3, 3, 4, 4]
        max_count = 1
        count = 1
        mode = None
        for i in range(1, len(sorted_input)):
            if sorted_input[i] == sorted_input[i - 1]:
                count = count + 1
            else:
                if count > max_count:
                    max_count = count
                    mode = sorted_input[i - 1]
                count = 1

            if count > max_count:
                mode = sorted_input[i]

        if mode is not None:
            return mode
        else:
            return "Cannot find mode"


a1 = Ari([1, 2, 4, 8, 9])
print("Median", a1.median())
print("Mean", a1.mean())
print("Mode", a1.mode())


# Create a program to validate the age of the voter with the help of custom exception. Voters whose age is less than
# 18 should not be allowed to vote.

class InvalidAgeException(Exception):
    pass


class Voter:
    def __init__(self, age):
        self.age = age

    def eligibility(self):
        if self.age < 18:
            raise InvalidAgeException


v1 = Voter(12)
try:
    v1.eligibility()
except InvalidAgeException:
    print("Exception occurred for invalid age")


# Create a program to check eligibility of the person for loan  with the help of oops concepts and exception
# handling. Person whose salary is less than 10K/ Month will not be eligible for the loan.

class InvalidSalaryException(Exception):
    print("Invalid Salary Exception")
    pass


class Employee:
    def __init__(self, salary):
        self.salary = salary

    def eligibility(self):
        if self.salary < 10000:
            raise InvalidSalaryException


e1 = Employee(1200)
try:
    e1.eligibility()
except InvalidSalaryException:
    print("Exception occurred for invalid salary")
