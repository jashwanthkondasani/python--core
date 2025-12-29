my_array=[11,23,45,67,2,1]
minVal=my_array[0]
for i in my_array:
        if i<minVal:
            minVal=i
print("minimum value in the array is:", minVal)   

stack=[]
stack.append(10)
stack.append(20)
stack.append(30)
print("Stack after pushing elements:", stack) 

topElement = stack[-1] if stack else None
print("Top element in the stack:", topElement)


poppedElement = stack.pop() if stack else None
print("Popped element from the stack:", poppedElement)
