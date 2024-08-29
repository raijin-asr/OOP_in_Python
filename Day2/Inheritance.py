"""Python Inheritance
--In Python object oriented Programming, Inheritance is the capability of one class to derive or inherit the properties from another class.
--The class that derives properties is called the derived class or child class and the class from which the properties are being derived is called the base class or parent class.

The benefits of inheritance are:
--It represents real-world relationships well.
--It provides the reusability of a code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.
--It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.

Types of Inheritance
--Single Inheritance: Single-level inheritance enables a derived class to inherit characteristics from a single-parent class.
--Multilevel Inheritance: Multi-level inheritance enables a derived class to inherit properties from an immediate parent class which in turn inherits properties from his parent class. 
--Hierarchical Inheritance: Hierarchical-level inheritance enables more than one derived class to inherit properties from a parent class.
--Multiple Inheritance: Multiple-level inheritance enables one derived class to inherit properties from more than one base class."""


# Python code to demonstrate how parent constructors are called.
# parent class
class Person(object): # Single Inheritance

    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)
        
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
    
# child class
class Employee(Person): #Person argument is parent class
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber) # inheritance
        
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
        print("Post: {}".format(self.post))


# creation of an object variable or an instance
a = Employee('Ram', 886012, 200000, "Intern")

# calling a function of the class Person using
# its instance
a.display()
a.details()

# Output
# Ram
# 886012
# My name is Ram
# IdNumber: 886012
# Post: Intern

#Multi-level Inheritance:--------------
class Bike: #parent class
    @staticmethod
    def start():
        print("Bike started...")

    @staticmethod
    def stop():
        print("Bike stopped...")

class Hero(Bike): #child class Hero inheriting parent class Bike
    def __init__(self, brand):
        self.brand= brand
    
class Extreme(Hero): #grand child Extreme inheriting child bike
    def __init__(self, type):
        self.type= type

bike1= Extreme("petrol")  #creating object of Extreme class
print(bike1.type) #petrol
print(bike1.brand) #Error

bike1.stop() #Bike stopped...
bike1.start() #Bike started...

print(bike1.brand) #Error
# using brand in Extreme class will give error because brand is not defined in Extreme class. It is defined in Hero class. So, we can access brand using object of Hero class.
# so we can access brand using object of Hero class.
bike1= Hero("Hero")
print(bike1.brand) #Hero

#Hierarchical Inheritance:--------------
class Bike: #parent class
    @staticmethod
    def start():
        print("Bike started...")

    @staticmethod
    def stop():
        print("Bike stopped...")

class Hero(Bike): #child class Hero inheriting parent class Bike
    def __init__(self, brand):
        self.brand= brand

class Honda(Bike): #child class Honda inheriting same parent class Bike
    def __init__(self, brand):
        self.brand= brand

bike1= Hero("Hero")  #creating object of Hero class

bike1.stop() #Bike stopped...
bike1.start() #Bike started...

bike2= Honda("Honda")  #creating object of Honda class

bike2.stop() #Bike stopped...
bike2.start() #Bike started...


#Multiple Inheritance:--------------
class Bike: #parent class
    @staticmethod
    def start():
        print("Bike started...")

    @staticmethod
    def stop():
        print("Bike stopped...")

class Car: #another parent class
    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("Car stopped...")

class Vehicle(Bike, Car): #child class Vehicle inheriting two parent class Bike and Car
    def __init__(self, brand):
        self.brand= brand

    def drive(self):
        self.start()
        print(f"{self.brand} is driving...")
        self.stop()

bike1= Vehicle("Hero")  #creating object of Vehicle class
bike1.drive() 
#Bike started...
# Hero is driving...
# Bike stopped...

bike2= Vehicle("Honda")  #creating object of Vehicle class
bike2.drive()
#Bike started...
# Honda is driving...
# Bike stopped...

car1= Vehicle("Car")  #creating object of Vehicle class
car1.drive()
#Car started...
# Car is driving...
# Car stopped...

#Python super() function
#Python super() function provides us the facility to refer to the parent class explicitly. 
# It is basically useful where we have to call superclass functions.

class Bike: #parent class
    @staticmethod
    def start():
        print("Bike started...")

    @staticmethod
    def stop():
        print("Bike stopped...")

class Car: #another parent class
    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("Car stopped...")

class Vehicle(Bike, Car): #child class Vehicle inheriting two parent class Bike and Car
    def __init__(self, brand):
        self.brand= brand

    def drive(self):
        super().start() #super() function is used to call the parent class function
        print(f"{self.brand} is driving...")
        super().stop()

bike1= Vehicle("Hero")  #creating object of Vehicle class
bike1.drive() 
#Bike started...
# Hero is driving...
# Bike stopped...















