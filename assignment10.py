#Q1 Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.
class Circle():
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        print("Area is : " + str(3.14 * self.radius * self.radius))

    def getCircumference(self):
        print("Circumference is: " + str( self.radius * 2 * 3.14))

ob=Circle(float(input('enter the radius:')))
ob.getArea()
ob.getCircumference()

#Q2 Create a Student class and initialize it with name and roll number.
class Student():
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print(self.name)
        print(self.roll)

ob= Student(input("Enter name of student : "), input("Enter his/her roll no : "))
ob.display()


#Q3 Create a Temprature class.
class Temperature():
    def convertfahrenheit(self, celsius):
        print("Temperature in Fahrenheit is : " + str((celsius * (9 / 5)) + 32))

    def convertcelsius(self, farenheit):
        print("Temperature in Celsius is : " + str((farenheit - 32) * (5 / 9)))


ob = Temperature()
ob.convertfahrenheit(int(input("Enter temperature in Celsius : ")))
ob.convertcelsius(int(input("Enter temperature in Fahrenheit : ")))

#Q4 Create a class MovieDetails and initialize it with Movie name, artistname,Year of release and ratings.
class moviedetails():
    def __init__(self, moviename, artistname, yor, ratings):
        self.moviename = moviename
        self.artistname = artistname
        self.yor = yor
        self.ratings = ratings

    def display(self):
        print("Movie name is :" + str(self.moviename))
        print("Artist name is " + str( self.artistname))
        print("Year of release is " + str (self.yor))
        print("Rating is " + str( self.ratings))

    def update(self):
        self.moviename = input("enter updated Movie name      : ")
        self.artistname = input("enter updated Artist name     : ")
        self.yor = input("enter updated Year of release : ")
        self.ratings = input("enter updated Ratings         : ")

ob = moviedetails('ZNMD', 'HRITIK', '2011', '8.1')
ob.display()
ob.update()
ob.display()

#Q5 Create a class Expenditure and initialize it with expenditure,savings.Make the following methods.
class Expenditure:
    def __init__(self):
        self.expenditure = int(input("Total expenditure of the month is: "))
        self.savings = int(input("Total savings of the month is: "))

    def display(self):
        print("Total expenditure of the month is : ",self.expenditure)
        print("Total savings of the month is : ",self.savings)

    def salary(self):
        self.total_salary = self.expenditure+self.savings

    def DisplaySalary(self):
        print("Total salary of the month is: ",self.total_salary)

ob = Expenditure()
ob.display()n
ob.salary()
ob.DisplaySalary()