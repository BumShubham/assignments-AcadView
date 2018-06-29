#Q1. Create a thread that sleeps for 5 seconds & prints a message
from threading import Thread                                            #Import Thread class from threading library to handle threads
from time import sleep                                                  #Import sleep class from time library to cause delays
import math
import threading


def thread_sleep(arg,name):                                             #Function to make the thread sleep
  for i in range(arg):                                                  #For loop running until the argument count exceeds
    print("Acessing %s's thread for %dth time" % (name, i+1))
    sleep(5)

def run():                                                               #Function to initialize threads
    thread = Thread(target = thread_sleep, args = (5,'Shubham', ))       #Creation of new thread with positional arguments
    thread.start()                                                       #Inbuilt method call start() to start threading
    thread.join()                                                        #Raises a RuntimeError if an attempt to join the current thread as to avoid deadlock.
    print ("Thread Finished... Exiting")
run()                                                                    #Function call to invoc run()

#Q2. Make a thread that prints numbers 1-10 & sleeps for 1 seconds regularly

def print_numbers(arg):                                                  #Function to print numbers from 1-10 with delay
  for i in range(arg):                                                   #For loop running until argument count (here 10) exceeds
    print("%d" % ( i+1))
    sleep(1)                                                             #Sleep for 1 unit time

def handle_thread():                                                     #Function to initialize threads
    thread = Thread(target = print_numbers, args = (10, ))               #Creation of new thread with positional arguments
    thread.start()
    thread.join()
    print ("Thread Finished... Exiting")
#Driving Code
handle_thread()                                                          #Function call to invoc handle_thread()

#Q3. Create a list & print it's elements with delay in multiple of 2

def print_list(arg,listName, delay):                                     #Function to print elements of list with delays
  for i in range(arg):
    print("%s" % (listName[i]))
    delay = delay*2                                                      #increase delay in the power of 2
    sleep(delay)                                                         #Sleep for given amount of delay

def list_handler(listName):                                              #Function to initialize threading process
    thread = Thread(target = print_list, args = (5, listName, 1))        #Creation of new thread with positional arguments
    thread.start()
    thread.join()
    print ("Thread Finished... Exiting")

sample = ["Mission Impossible: Fallout", "Incredibles 2", "Padman", "Deadpool 2", "YJHD"]     #List with sample elements
list_handler(sample)                                                                             #Function call with list as parameter

#Q4. Call factorial function using thread
def fact():
    no=int(input('enter a no'))
    res=math.factorial(no)
    print(res)

threading.Thread(target=fact).start()