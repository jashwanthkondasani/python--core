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

 creating a class 
class Student:
      name="jashwanth"
      age=20


  # creating object of class
s1=Student()
print(s1.name)
print(s1.age)

class car:
    color="red"
    price=1000000

c1=car()
print(c1.color)
print(c1.price)

 creating a class with init method 
class student :
    def __init__(self, name, age):
        self.name=name
        self.age=age
        #  creating a method 
    def display(self):
        print("name:", self.name)
        print("age:", self.age)
#  creating an object of class 
s1=student("jashwanth", 20)
s1.display()
class student :
    college_name="sri venkateswara college of engineering  "
    name ="jashwanth kumar redddy "

    def __init__(self, name,marks):
        self.marks=marks
        self.name=name
        print("adding new student into database ")

s1=student("svce", "jashwanth")
print(s1.college_name)
print(s1.name)  

def display(self):
    print("college name:", self.college_name)
    print("name:", self.name)

def get_avg():
    sum=0
    for mark in self.marks:
        sum+=val
        print("average marks:", sum/len(self.marks))

s1=student("jashwanth", [90, 85, 88, 92, 79])

s1.get_avg()


 
