"""
@property method is used to access the class attributes as a method.
Python property() function returns the object of the property class and it is used to create the property of a class.
the property() function is a built-in function that allows us to create a property for a class


Syntax: property(fget, fset, fdel, doc)

Parameters: 
fget() - used to get the value of attribute
fset() - used to set the value of attribute
fdel() - used to delete the attribute value
doc() - string that contains the documentation (docstring) for the attribute

Return: Returns a property attribute from the given getter, setter and deleter.

Note:
--If no arguments are given, property() method returns a base property attribute that doesn’t contain any getter, setter, or deleter.
--If doc isn’t provided, property() method takes the docstring of the getter function.
"""

#What is property() Function in Python?
"""
Python property() function is a built-in function that allows us to create a special type of attribute called a property for a class. 
Properties are used to encapsulate the access to an object attribute and to add some logic to the process such as computation, access control, or validation.

Python property() Function Methods
Below are the ways by which we can create property for a class in Python:

a) Using property() method
b) Using @property decorator
"""

#Using property() Method :
# In this example, we are using the property() function to create a class property in Python. 
# We define a class called Alphabet, and within this class, we create a property named value to encapsulate access to an internal attribute _value. 
# This property allows us to control how the _value attribute is accessed and modified by providing custom getter and setter methods.

# Python program to demonstrate property()
# Python program to explain property() function
# Alphabet class

class Alphabet:
    def __init__(self, value):
        self._value = value

    # getting the values
    def getValue(self):
        print('Getting value')
        return self._value

    # setting the values
    def setValue(self, value):
        print('Setting value to ' + value)
        self._value = value

    # deleting the values
    def delValue(self):
        print('Deleting value')
        del self._value

    value = property(getValue, setValue, 
                     delValue, )

# passing the value
x = Alphabet('GeeksforGeeks')
print(x.value)

x.value = 'GfG'

del x.value

# Output:

# Getting value
# GeeksforGeeks
# Setting value to GfG
# Deleting value

"""
Using @property Decorator:
The main work of decorators is they are used to add functionality to the existing code. 
Also called metaprogramming, as a part of the program tries to modify another part of the program at compile time. 

First, specify that value() method is also an attribute of Alphabet then, we use the attribute value to specify the Python property setter and the deleter.
Notice that the same method value() is used with different definitions for defining the getter, setter, and deleter. 
Whenever we use x.value, it internally calls the appropriate getter, setter, and deleter.

"""
# Python program to explain property() function using decorator

class Alphabet:
    def __init__(self, value):
        self._value = value

    # getting the values
    @property
    def value(self):
        print('Getting value')
        return self._value

    # setting the values
    @value.setter
    def value(self, value):
        print('Setting value to ' + value)
        self._value = value

    # deleting the values
    @value.deleter
    def value(self):
        print('Deleting value')
        del self._value


# passing the value
x = Alphabet('Peter')
print(x.value)

x.value = 'Diesel'

del x.value

# Output:
# Getting value
# Peter
# Setting value to Diesel
# Deleting value

"""Python Property vs Attribute:
Class Attribute: Class Attributes are unique to each class. 
    Each instance of the class will have this attribute. 
In the given example, the count variable is a class attribute."""

# declare a class
class Employee:

    # class attribute
    count = 0

    # define a method
    def increase(self):
        Employee.count += 1

# create an Employee
# class object
a1 = Employee()

# calling object's method
a1.increase()

# print value of class attribute
print(a1.count)

a2 = Employee()

a2.increase()

print(a2.count)

print(Employee.count)

#OUtput:
# 1
# 2
# 3

#Simple example of @property decorator: where marks of physics changes after correcting marks from 90 to 88
class Student:
    def __init__(self, name, phy,math):
        self.name = name
        self.phy = phy
        self.math = math

    @property #decorator to make it property to access as method and change automatically
    def marksCorrected(self):
        return str((self.phy+ self.math)/2)
    
st1= Student("Ram", 90, 80)
print(st1.marksCorrected) #85.0
st1.phy = 88
print(st1.marksCorrected) #84.0 , automatically changes after changing phy marks
