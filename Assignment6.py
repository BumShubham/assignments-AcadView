#Q1 Take 10 integers from user and print it on screen.
print("enter the elements:")
for i in range(10):
    a=int(input())

#Q2 Write an infinite loop.An infinite loop never ends. Condition is always true.
'''while (1):
    print('true')
'''

#Q3 Create a list of integer elements by user input. Make a new list which will store square of elements of previous list.
list = []
print('enter the int elements')
list = [int(y) for y in input().split()]
print(list)
def square(list):
    ret = []
    for i in list:
        ret.append(i ** 2)
    return ret
print(square(list))


#Q4 From a list containing ints, strings and floats, make three lists to store them separately
list=[1,2,3,'shubham',3.6,8.7,1.1,'saxena','messi']
nolist= [x for x in list if isinstance(x, int)]
strlist=[x for x in list if isinstance(x, str)]
floatlist=[x for x in list if isinstance(x, float)]
print(nolist)
print(strlist)
print(floatlist)

#Q5 Using range(1,101) make a list containing even and odd numbers.
even=[]
odd=[]
for i in range(1,101):
  if i%2 == 0:
    even.append(i)
  else:
    odd.append(i)
print(even)
print(odd)

#Q6 Pattern
for i in range(0,4) :
    for j in range(0,i+1) :
        print("*",end=" ")
    print()


#Q7 User defined Dictionary
dict = {'shubham' : 22, 'saxena' : 21,'messi' : 31}
for key in dict.keys():
    print(key,dict[key])


#Q8 Element found and delete
print('enter the elements in list:')
list = [int(x) for x in input().split()]
print(list)
num = int(input('enter number to be removed:'))
for i in list:
    if i == num:
        print('found')
list.remove(num)
print(list)