# [“name512”, “same1example”, “joy18full”] replace the digits from string inside list
import datetime
import random
import re

i_ = ["name512", "same1example", "joy18full"]


def replace_func(i_str):
    return "".join(re.findall('[a-zA-Z]', i_str))


output = map(replace_func, i_)
print(list(output))

# [1, “a”, 2, “b”, 3, “c”] filter digits and alphabets separately using inbuilt functions like map, filter or reduce
digits = []
alphabets = []


def segregate(a):
    if type(a) is int:
        digits.append(a)
    elif type(a) is str:
        alphabets.append(a)


i2_input = [1, "a", 2, "b", 3, "c"]
result = map(segregate, i2_input)
print("Digits", digits)
print("Alphabets", alphabets)


#
# str1 = []
# i3_input = [1, "a", 2, "b", 3, "c"]
# result1 = filter(lambda a: if type(a) is int i3_input.pop(a), i3_input)
# print("POPPED", list(result1))
# print("LEFT", i3_input)


# Create function to generate data randomly with python standard library
# num = random.random()
# print(num)


def generate_random_data(num_samples):
    data = []
    for i in range(num_samples):
        data.append(int(round(random.uniform(1, 100), 0)))
    return data


print("generate_random_data", generate_random_data(5))

# [1,2,3,1,3,4,6,5,3] get unique numbers from list with basic constructs

print(set([1, 2, 3, 1, 3, 4, 6, 5, 3]))
i4_input = [1, 2, 3, 1, 3, 4, 6, 5, 3]
new_set = set()
for i in i4_input:
    new_set.add(i)

print("Unique Set", new_set)


# Create function to check if date is in given range
date1 = "20/01/2026"
date2 = "20/01/2025"
element1 = datetime.datetime.strptime(date1, "%d/%m/%Y")
element2 = datetime.datetime.strptime(date2, "%d/%m/%Y")

print(date1) if date1 > date2 else print(date2) if date2 > date1 else print('Same Date')