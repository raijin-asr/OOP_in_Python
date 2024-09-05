# Polymorphism simply means having many forms. 
# For example, we need to determine if the given species of birds fly or not, using polymorphism we can do this using a single function.

# In programming, polymorphism means the same function name (but different signatures) being used for different types. 
# The key difference is the data types and number of arguments used in function

# Python program to demonstrate in-built poly-morphic functions
# len() being used for a string
print(len("geeks"))

# len() being used for a list
print(len([10, 20, 30]))

# A simple Python function to demonstrate Polymorphism
def add(x, y, z = 0): 
    return x + y+z

# Driver code 
print(add(2, 3)) # prints 5
print(add(2, 3, 4)) # prints 9

# Python program to demonstrate Polymorphism: (class with inheritance)
# Creating a class
class Bird:
    def intro(self):
        print("There are many types of birds.")
    
    def flight(self):
        print("Most of the birds can fly but some cannot.")

# Creating a class
class sparrow(Bird): # sparrow class inherits the Bird class
    def flight(self): # overriding the flight method of Bird class
        print("Sparrows can fly.")

# Creating a class
class ostrich(Bird): # ostrich class inherits the Bird class
    def flight(self): # overriding the flight method of Bird class
        print("Ostriches cannot fly.")

# Driver code
obj_bird = Bird()
obj_spr = sparrow() 
obj_ost = ostrich()

obj_bird.intro() # output: There are many types of birds.
obj_bird.flight() # output: Most of the birds can fly but some cannot.

obj_spr.intro() # output: There are many types of birds.
obj_spr.flight() # output: "Sparrows can fly." | as it overrides the flight method of Bird class

obj_ost.intro() # output: There are many types of birds.
obj_ost.flight()    # output: "Ostriches cannot fly." | as it overrides the flight method of Bird class

# What is the role of abstract base classes in polymorphism?
# Abstract base classes (ABCs) define a common interface for a group of subclasses. 
# They cannot be instantiated themselves and require subclasses to provide implementations for their abstract methods. 
# ABCs ensure that derived classes adhere to a specific protocol, thus supporting polymorphism.

# Example:
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.sound())
# Output:
# Bark
# Meow



"""Polymorphism with class methods: 

The below code shows how Python can use two different class types, in the same way. 
We create a for loop that iterates through a tuple of objects. 
Then call the methods without being concerned about which class type each object is. 
We assume that these methods actually exist in each class. """

class India():
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")

class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")

obj_ind = India()
obj_usa = USA()

for country in (obj_ind, obj_usa): #iterating through a tuple of objects
    country.capital()
    country.language()
    country.type()

# Output:
# New Delhi is the capital of India.
# Hindi is the most widely spoken language of India.
# India is a developing country.
# Washington, D.C. is the capital of USA.
# English is the primary language of USA.
# USA is a developed country.


"""Polymorphism with a Function and objects: 
It is also possible to create a function that can take any object, allowing for polymorphism.

In this example, let’s create a function called “func()” which will take an object which we will name “obj”. 
Though we are using the name ‘obj’, any instantiated object will be able to be called into this function. 
Next, let’s give the function something to do that uses the ‘obj’ object we passed to it. 
In this case, let’s call the three methods, viz., capital(), language() and type(), each of which is defined in the two classes ‘India’ and ‘USA’. 
Next, let’s create instantiations of both the ‘India’ and ‘USA’ classes if we don’t have them already. 
With those, we can call their action using the same func() function: """

class Nepal():
    def capital(self):
        print("Kathmandu is the capital of Nepal.")
 
    def language(self):
        print("Nepali is the most widely spoken language of Nepal.")
 
    def type(self):
        print("Nepal is a developing country.")
 
class China():
    def capital(self):
        print("Beijing is the capital of China.")
 
    def language(self):
        print("Chinese is the primary language of China.")
 
    def type(self):
        print("China is a developed country.")

def func(obj): #function that can take any object
    obj.capital() #calling the capital method
    obj.language() #calling the language method
    obj.type() #calling the type method
 
obj_nepal = Nepal() #instantiating the object of Nepal class
obj_china = China() #instantiating the object of China class
 
func(obj_nepal)
func(obj_china)

# Output:
# Kathmandu is the capital of Nepal.
# Nepali is the most widely spoken language of Nepal.
# Nepal is a developing country.

# Beijing is the capital of China.
# Chinese is the primary language of China.
# China is a developed country.
