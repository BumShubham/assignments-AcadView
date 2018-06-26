#Q1
#What is time tuple
'''
Many of Python's time functions handle time as a tuple of 9 numbers, as shown below −
Index	Field	Domain of Values
0	Year (4 digits)	Ex.- 1995
1	Month	1 to 12
2	Day	1 to 31
3	Hour	0 to 23
4	Minute	0 to 59
5	Second	0 to 61 (60/61 are leap seconds)
6	Day of Week	0 to 6 (Monday to Sunday)
7	Day of Year	1 to 366 (Julian day)
8	DST	-1,0,1
'''

#Q2 Write a program to get formatted time.
import time
import math
import os
print(time.strftime("%H:%M:%S"))

#Q3 Extract month from the time.
'''The function strftime takes '2' arguments one format and another time strftime(format,t = time)
'''
print(time.strftime("%B,%m"))

#Q4 Extract day from the time
print(time.strftime("%d, %j"))

#Q5 Extract date (ex : 11 in 11/01/2021) from the time.
print(time.strftime("%d in %d/%m/%Y"))

#Q6 Write a program to print time using localtime method.
localtime = time.localtime(time.time())
print("Local current time :", localtime)

#Q7 Find the factorial of a number input by user using math package functions.
'''
Used to calculate factorial of a Number, using Math package function
Math.factorial(number) is used
'''

no=int(input('enter a no:'))
print(math.factorial(no))

#Q8 Find the GCD of a number input by user using math package functions.
'''
Used to calculate GCD of a number, using Math package function
Math.gcd(no1,no2) is used
'''

a=int(input('enter 1st no:'))
b=int(input('enter 2nd no:'))
print(math.gcd(a,b))

#Q9 Use OS package and do the following tasks:  Get current working directory.Get the user environment.
print(os.getcwd())
print(os.getenv('TEMP'))