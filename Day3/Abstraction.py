# Data Abstraction 
# It hides unnecessary code details from the user. Also,  when we do not want to give out sensitive parts of our code implementation and this is where data abstraction came.
# Hiding the implementation details and showing only the functionality to the user is known as abstraction.

#example of car printing car started and not showing how it is started.
class Car:
    def __init__(self):
        self.accelerator = False
        self.brake = False
        self.steering = False

    def start(self):
        self.accelerator = True
        print("Car started...")

car1= Car() #creating object of Car class
car1.start() #Car started...
#Output only showing Car started... and not showing how it is started. This is abstraction.
# it did not show value of accelerator, brake and steering. It only showed the functionality of start method.


# Data Abstraction in Python can be achieved by creating abstract classes.--------
# Python provides a module called abc (Abstract Base Class) which provides the base for defining Abstract Base classes.
# Abstract Base classes are classes that contain one or more abstract methods.
# Abstract methods are the methods that generally don’t have any implementation, it is left to the sub classes to provide implementation for the abstract methods.

# Python program showing abstract base class work
from abc import ABC, abstractmethod

class Car(ABC): #abstract class with ABC module
    #instance variables
    type= "electric"
    
    #constructor
    def __init__(self):
        pass 

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    #extra concrete methodsD
    def concrete(self):
        print("This is extra concrete method")

class Vehicle(Car):
    def start(self):
        print("Car started...")

    def stop(self):
        print("Car stopped...")

car1= Vehicle() #creating object of Vehicle class
car1.start() #Car started...
car1.stop() #Car stopped...
#In the above example, the Car class is an abstract class containing two abstract methods start() and stop().
#The Vehicle class is a subclass of the Car class and it provides the implementation of the abstract methods start() and stop().
#If we do not provide the implementation of the abstract methods in the subclass, it will give an error.


# Data Abstraction in Python can also be achieved by using interfaces.--------
# An interface is a class that contains only the method declarations without method definitions.
# An interface is used to specify what a class must do and not how. It is the blueprint of the class.
# Its like Boss ordering what things to do, and worker(subclass) define and do them how part.

# Python program showing interface work
from abc import ABC, abstractmethod

class Car(ABC):
    #NO instance variables

    #NO constructors

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    # here only abstract methods, NO other methods

class Vehicle(Car):

    def start(self):
        print("Car started...")

    def stop(self):
        print("Car stopped...")

car1= Vehicle() #creating object of Vehicle class
car1.start() #Car started...
car1.stop() #Car stopped...
#In the above example, the Car class is an interface containing two abstract methods start() and stop().
#The Vehicle class is a subclass of the Car class and it provides the implementation of the abstract methods start() and stop().
#If we do not provide the implementation of the abstract methods in the subclass, it will give an error.
#Interfaces are used to provide a way to define the structure of a class. It is a way to achieve abstraction in Python.

#difference between abstract class and interface in Python---------
#An abstract class can have both abstract methods and concrete methods.
#An interface can only have abstract methods.

#An abstract class can have instance variables.
#An interface cannot have instance variables.

#An abstract class can have constructors.
#An interface cannot have constructors.


#Another examples showing interfaces:
from abc import ABC, abstractmethod

# Interface-like class
class Drawable(ABC): #interface class does not have any implementation of methods
    @abstractmethod 
    def draw(self):
        pass

# Abstract base class (combining interface and implementation)
class Shape(Drawable, ABC): #this is abstract class
    #constructor
    def __init__(self, color): #abstract class with ABC module having constructor
        self.color = color

    #other concrete methods 
    def draw(self):
        print(f"Drawing a shape with color {self.color}")

class Circle(Shape): # child class inheriting parent class Shape
    def __init__(self, radius, color):
        super().__init__(color)
        self.radius = radius

    def draw(self):
        print(f"Drawing a circle with radius {self.radius} and color {self.color}")

class Square(Shape): # child class inheriting parent class Shape
    def __init__(self, side_length, color):
        super().__init__(color)
        self.side_length = side_length

    def draw(self):
        print(f"Drawing a square with side length {self.side_length} and color {self.color}")





