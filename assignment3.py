#Q1
list = []
f = float(input("1st element:"))
s = int(input("2nd  element:"))
t = input('3rd element:')
list.append([f,s,t])
print(list)

#Q2
list.append(['google','apple','facebook','microsoft','tesla'])
print(list)

#Q3
a=[1,2,1,4,2,3,2]
print(a)
print(a.count(1))
print(a.count(2))

#Q4
num=[1,2,5,9,3,7,8]
num.sort()
print(num)

#Q5
A=[1,3,4,7,8]
B=[9,2,10,11]
C= A + B
print(C)
C.sort()
print(C)

#Q6
#Stack using list
stack = ["saxena", "shubham", "bum"]
stack.append("mogambo")
stack.append("khush h")
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)


#Queue using lists
q = []
for i in range(0, 5):
    q.append(i)  # Add to back of queue
while q:  # Queue not empty
    j = q.pop(0)
    print(j)

#Optional Q

print(C)
e=0
o=0
for x in C:
        if not x % 2:
    	     e+=1
        else:
    	     o+=1
print("Number of even numbers : " , e)
print("Number of odd numbers : " , o)
