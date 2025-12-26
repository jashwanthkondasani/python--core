
# continue the word
for letter in "jashwanth kumar reddy":
    if letter == 'y':
        continue
    print(letter, end=' ')
print()
# break the word

for letter in "Python":
    if letter == 'y':
        break
    print(letter, end=' ')
print()
# print multiplication table
n=int(input("enter the number"))
for i in range(1,11):
      print(f"{n}X{i}={n*i}")

# check weather prime or not
for i in range (2,n):
      if(n%i)==0:
            print(" number is not prime")
      else:
            print("number is not prime")

import numpy as np
a = np.array([1, 2, 3, 4])

# Element-wise operations
print(a * 2)  

# Multi-dimensional array
res = np.array([[1, 2], [3, 4]])
print(res * 2)

#  factorial using recursion
def fact(n):
    if n==0 :
        return 1
    return n*fact(n-1)
print(fact(3))

# print 5 times in a loop
count=1
while(count<=2):
      print("jai sri ram")
      count+=1

# find power of number using recursion
def power(n,p):
        if p==0:
                return 1
        return n*power(n,p-1)
print(power(11,22))

#  check wether number is prime or not prime\

def prime(n,i=2):
      if n<=2:
            return True if n==2 else False
      if n%i==0:
            return False
      if i*i>n:
            return True
      return prime(n,i+1)   
print(prime(22))

a=float(input("enter the number "))
b=float(input("enter the number "))
c=float(input("enter the number"))
 
if a==b==c:
   print("equilateral triangle")
elif a==b or b==c or c==a:
  print("isosceles triangle")
else:
    print("scalene triangle")

num = int(input("Enter a number: "))

if num > 0:
    print("Number is Positive")
    if num % 2 == 0:
        print("It is Even")
    else:
        print("It is Odd")
elif num == 0:
    print("Number is Zero")
else:
    print("Number is Negative")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b:
    if a > c:
        print("a is the largest")
    else:
        print("c is the largest")
else:
    if b > c:
        print("b is the largest")
    else:
        print("c is the largest")

 programms by using loops 
count=0
while(count<3):
    print("hello jashwanth kumar reddy")
    count+=1

for num in range(1, 10):
    if num == 7:
        break
    print(num)


for num in range(1, 10):
    if num %2==0:
        continue
    print(num)

 sum of numbers for using loops

n = 11
total = 0
for i in range(1, n+1):
    total += i
print("Sum:", total)

n=11
total=0
for i in range (1 ,n+1):
      total=total+i
print("sum:",total)

rows=5
for i in range(1, rows+1):
  print('*'* i)
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))

print(" choose an operator ")
print(" + addition ")
print(" - subtraction ")
print(" * multiplication ")
print(" / division ")

op=input("enter operator (+,-,*,/)")

if op=='+':
   print("result:", num1+num2)

elif op=='-':
   print("result:", num1-num2)

elif op=='*':
   print("result:", num1*num2)

elif op=='/':
   if num2 !=0:
       print("result:", num1/num2)
   else:
       print("Error: Division by zero is not allowed.")
else:
   print("Invalid operator")

 using  functions 
def calculator(a,b,op):
     if op=='+':
         return a+b
     elif op=='-':
         return a-b
     elif op=='*':
         return a*b
     elif op=='/':
         if b !=0:
             return a/b
         else:
             return "Error: Division by zero is not allowed."
     else:
         return "Invalid operator"
     
 print(calculator(10,5,'+'))
 print(calculator(10,5,'-'))
 print(calculator(10,5,'*'))
 print(calculator(10,5,'/'))
 print(calculator(10,0,'/'))
 print(calculator(10,5,'^'))

