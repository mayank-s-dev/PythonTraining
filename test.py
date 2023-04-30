# importing pandas module
import pandas as pd

# reading csv file from url
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# dropping null value columns to avoid errors
data.dropna(inplace=True)

# joining string and overwriting
data["Name"] = data["Name"].str.join("-")

# display
# print(data, type(data))

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)
# print(df.l)

from datetime import date


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  # a class method to create a
  # Person object by birth year.
  @classmethod
  def fromBirthYear(cls, name, year):
    return cls(name, date.today().year - year)

  def display(self):
    print("Name : ", self.name, "Age : ", self.age)


person = Person('mayank', 21)
a = person.fromBirthYear("hello", 2991)
print(a.name)