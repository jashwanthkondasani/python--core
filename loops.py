
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
