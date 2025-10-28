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
