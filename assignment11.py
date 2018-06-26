#Q1
class Animal():
    '''
    This class is made to showcase some features of Animal class
    '''
    legs = 4
    eyes = 2
    ears = 2

    def Animal_attribute(self):
        '''
            This method is used to show some features of Animal
        Parameters
        ----------
        legs - tells how many legs does Animals have
        eyes - tells how many eyes does Animals have
        ears - tells how many ears does Animals have
        Returns
        --------
        '''
        print('%d legs' % self.legs)
        print('%d eyes' % self.eyes)
        print('%d ears' % self.ears)


class Tiger(Animal):
    def __init__(self):
        self.Animal_attribute()



ob=Tiger()

#Q2
# A  B
# A  B

#Q3
#Create a class Cop. Initialize its name, age , work experience and designation.
#Define methods to add, display and update the following details.
# Create another class Mission which extends the class Cop. Define method add_mission _details.
#Select an object of Cop and access methods of base class to get information for a particular cop and make it available for mission

class Cop():
    '''
    This class is made to show show details of a cop
    '''
    def __init__(self,name,age,workexp,desig):
        self.name=name
        self.age=age
        self.workexp=workexp
        self.desig=desig

    def Add(self):
        self.name = input("Enter name: ")
        self.age = input("Enter age   : ")
        self.workexp = input("Enter work experience : ")
        self.desig = input("Enter designation     : ")

    def Display(self):
        print("Name of cop : " + str(self.name))
        print("Age of cop  : " + str(self.age))
        print("Work experience of cop : " + str(self.workexp))
        print("Designation of cop     : " + str(self.desig))

    def Update(self):
        '''
        This method is used to update the cop details
        '''
        self.name = input("Enter name : ")
        self.age = input("Enter age   : ")
        self.workexp = input("Enter work experience : ")
        self.desig = input("Enter designation     : ")

class Mission(Cop):
    def add_mission_details(self):
        print("\nCOP IS READY FOR MISSION.......")

ob= Cop('name', 'age', 'work experience', 'designation')
ob.Add()
ob.Display()
ob.Update()
ob.Display()


#Q4
#Create a class Shape.Initialize it with length and breadth Create the method Area.
#Create class rectangle and square which inherits shape and access the method Area.

class Shape():

    def __init__(self,length,breadth):
        self.length= length
        self.breadth= breadth

    def Area(self):
        print("Area is : " + str(self.length * self.breath))

class Rectangle(Shape):
    '''
    This class inherit Shape class method.
    '''
    def __init__(self, length, breath):
        self.length = length
        self.breath = breath

class Square(Shape):
    '''
    This class also inherit shape class.
    '''
    def __init__(self, length, breath):
        self.length = length
        self.breath = breath

rect1 = Rectangle(int(input("Enter length of rectangle : ")), int(input("Enter breath of rectangle : ")))
rect1.Area()

square1 = Square(4, int(input("Enter breath of square : "))) #as area is 4 times the side
square1.Area()