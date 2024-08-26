"""What is Object-Oriented Programming in Python?
In Python object-oriented Programming (OOPs) is a programming paradigm that uses objects and classes in programming. 
It aims to implement real-world entities like inheritance, polymorphisms, encapsulation, etc. in the programming. 
The main concept of object-oriented Programming (OOPs) or oops concepts in Python is to bind the data and the functions that work together as a single unit so that no other part of the code can access this data. 

OOPs Concepts in Python
--Class in Python
--Objects in Python
--Polymorphism in Python
--Encapsulation in Python
--Inheritance in Python
--Data Abstraction in Python"""

# Class in Python:
# A class is a collection of objects. 
# A class contains the blueprints or the prototype from which the objects are being created. 
# It is a logical entity that contains some attributes and methods. 

"""Class Definition Syntax:

class ClassName:
   # Statement-1
   .
   .
   .
   # Statement-N
"""

# Examples:
class Student:
    # Class definition
    name = "John"
    age = 20

"""
Python Objects
In object oriented programming Python, The object is an entity that has a state and behavior associated with it. 
It may be any real-world object like a mouse, keyboard, chair, table, pen, etc.
 Integers, strings, floating-point numbers, even arrays, and dictionaries, are all objects. 
 More specifically, any single integer or any single string is an object. 
The number 12 is an object, the string “Hello, world” is an object, a list is an object that can hold other objects, and so on. 

An object consists of:
State(or Attributes): It is represented by the attributes of an object. It also reflects the properties of an object.
Behavior: It is represented by the methods of an object. It also reflects the response of an object to other objects.
Identity: It gives a unique name to an object and enables one object to interact with other objects.

"""

# Creating an object of the class Student
s1 = Student()
print(s1.name) # Output: John
print(s1.age) # Output: 20


# __init__() method in Python
# The __init__ method is similar to constructors in C++ and Java.
# Constructors are used for instantiating an object.
# The task of constructors is to initialize(assign values) to the data members of the class when an object of class is created.
# Like methods, a constructor also contains a collection of statements(i.e. instructions) that are executed at the time of Object creation.

# All classes have a function called __init__(), which is always executed when the object is being
#  initiated.

 #creating class
class Person: 
    def __init__(self, fullname):
        self.name =  fullname
 
#creating object
p1 =  Person("Ram" )
print(p1.name)  # Output: Ram

p2= Person("Shyam")
print(p2.name) # Output: Shyam

# *The self parameter is a reference to the current
#  instance of the class, and is used to access variables
#  that belongs to the class.

# Methods
#  Methods are functions that belong to objects.

 #creating class
class Employee:
    def __init__(self, fullname):
        self.name =  fullname #object attribute > class attribute
    
    def hello(self): # Method, self is mandatory as it is a reference to the current instance of the class
        print("hello", self.name)

 #creating object
e1 =  Employee("Ram" )
e1.hello() # Output: hello Ram

#static method: 
# A static method is a method that doesn't take a reference to the instance as its first argument.
# Methods that don’t use the self parameter (work at class level)
 
class EmployeeX:
    def __init__(self, fullname):
        self.name =  fullname #object attribute > class attribute
    
    @staticmethod #decorator to make it static method
    def hello():
        print("hello")

 #creating object
e1 =  EmployeeX("Ram" )
e1.hello() # Output: hello

#  *Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it
# decorators are used to modify the behavior of function or class method. and returns a new function or class method.
