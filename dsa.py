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

queue=[]
queue.append(10)
queue.append(20)
queue.append(30)
print("Queue after enqueuing elements:", queue)

frontElement = queue[0] if queue else None
print("Front element in the queue:", frontElement)

dequeuedElement = queue.pop(0) if queue else None
print("Dequeued element from the queue:", dequeuedElement)

class car:
   def __init__(self,color,price):
       self.color=color
       self.price=price

car1=car("red", 1000000)
car2=car("blue", 2000000)
car3=car("green", 3000000)

print("car color:", car1.color)
print("car color:", car2.color)
print("car color:", car3.color)
print("car price:", car1.price)
print("car price:", car2.price)
print("car price:", car3.price)
