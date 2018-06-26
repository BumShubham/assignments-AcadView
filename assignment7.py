#Q1
rad=float(input("enter the radius:"))
def area(radius):
    radius= 3.14*rad*rad
    print("area of circle is:%f" % radius )
print(area(rad))

#Q2
def perfect(a) :
    sum = 0
    for i in range(1,a) :
        if a % i == 0 :
            sum = sum + i

    if sum == a :
        return True
    else:
        return False

for i in range(1,1001) :
    if perfect(i):
        print(i)

#Q3
def table(n, t=1):
    if t == 11:
        return
    print(str(n) + " x " + str(t) + " = " + str(n*t))
    table(n, t+1)

table(int(input("Enter number: ")))


#Q4
def power(a,b) :
    if b == 0:
        return 1
    if b >= 1 :
        return a*power(a,b-1)

print(power(2,3))




#Q5
def fact(num,list):
    if num==0:
        return 1
    else:
        list.append(num)
        print(list)
        return num*fact(num-1,list)

list = []
number = int(input("Enter the number"))
print(fact(number,list))
