# ------------------------------------------strings in python------------------------------------------------------
                                             5/11/2025
s="nani kondasani"
print(s[0]) 

s = "GeeksforGeeks"
print(s[1:4])    # characters from index 1 to 3
print(s[:3])     # from start to index 2
print(s[3:])     # from index 3 to end
print(s[::-1])   # reverse string


s="allu arjumn" 
for char in s:    # characters from index 0 to
    print(char)

s = "nani kondasani"
s="n"+s[1:]
print(s)

s = "ruturaj gaikwad"
s1 = "r" + s[1:]                   # update first character
s2 = s.replace("geeks", "GeeksforGeeks")  # replace word
print(s1)\
print(s2)

convert into upper and lower cases 
 s="CHANGE"
print((s.lower()))

s="change matters "
print((s.upper ()))

 s = "My name is {} and I am {} years old.".format("jashwanth kondasani ", 22)
print(s)


 # =--------------------------------------------lists in python ------------------------------------------------
                                                6/11/25
j=[1,2,3,4,5]    
a=["nani","jash","sunil","nikhil"]
s=[1,"jash",2.5,True]
print(j)
print(a)
print(s)

a = [2] * 10
b = [0] * 6

print(a)
print(b)

a = [10, 20, 30, 40, 50]
print(a[0])    
print(a[-1])
print(a[1:4])   # elements from index 1 to 3

a = []
# append
a.append(10)  
print("After append(10):", a)  
#  insert
a.insert(0, 5)
print("After insert(0, 5):", a) 
#  extend 
a.extend([15, 20, 25])  
print("After extend([15, 20, 25]):", a) 
#  clear 
a.clear()
print("After clear():", a)

#  tuples in datastructures 

#  list using in stack in datastructures
stack=[]
stack.append('a')
stack.append('b')
stack.append('c')
print("Initial stack:", stack)
#  pop operation 
stack.pop()
print("Stack after pop():", stack)
print("Top element is:", stack[-1]) 

#  pop using in datastructures 
queue=[]
queue.append('a')
queue.append('b')
queue.append('c')
print("Initial queue:", queue)
#  pop operation 
queue.pop()
print("queue after pop():", queue)
print("Top element is:", queue[-1]) 
