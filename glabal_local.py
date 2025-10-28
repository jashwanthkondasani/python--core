
def greet():
    msg="hello this is jashwanth kumar reddy"
    print(msg)
greet()

msg = "jashwanth kumar reddy"
def greet_global():
    print("Inside:",msg)   # Accessing global variable inside the function

greet_global()
print("Outside:",msg)

def fun():
  print("inside",msg)
msg="jashwanth kumar reddy"
fun()
print("outside",msg)

def fun():
    global s
    s += "nani"
    print(s)
s = "nani kondasani "
fun()
print("Outside Function: ", s)

x = 99

def change():
    global x
    x = x + 99
    print("Inside function:", x)

change()
print("Outside function:", x)

# example to not writtem
def my_function():
    x = 10   # local variable
    print("Inside function:", x)

my_function()
print(x)  # ❌ Error! x is not accessible outside
