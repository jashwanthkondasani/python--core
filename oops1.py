# print("jai sri ram")

print("oops concepts ") 

# create class and object in python
class Student:
    # Constructor (special method to initialize object)
    def __init__(self, name, age):
        self.name = name   # instance variable
        self.age = age

    # Method (function inside a class)
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")