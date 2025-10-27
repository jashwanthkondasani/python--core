
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
