"""Python Encapsulation
It describes the idea of wrapping data and the methods that work on data within one unit. 
This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. 
To prevent accidental change, an object’s variable can only be changed by an object’s method. 
Those types of variables are known as private variables."""

# A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc

# Python program to demonstrate private members
# "__" double underscore represents private attribute. 
# Private attributes start with "__".

# Creating a Base class
class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"  # private member

# Creating a derived class
class Derived(Base):
    def __init__(self):

        # Calling constructor of Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)

# Driver code
obj1 = Base()
print(obj1.a) # prints GeeksforGeeks

# Uncommenting print(obj1.c) will raise an AttributeError

# Uncommenting obj2 = Derived() will also raise an AtrributeError as private member of base class is called inside derived class

# A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc. 
# The goal of information hiding is to ensure that an object’s state is always valid by controlling access to attributes that are hidden from the outside world.

# Consider a real-life example of  Encapsulation in a company involves separating departments (like sales and finance) and restricting direct data access. 
# To access data from another department, an official must request it through an authorized intermediary. 
# This ensures data security and prevents unauthorized access.

""" public, protected and private members in Python:------------
# In Python, there are 3 types of access modifiers:
# Public members: Members of a class that are accessible from anywhere are called public members.
# Protected members: Members of a class that are accessible from within the class and its subclasses are called protected members.
# Private members: Members of a class that are accessible from within the class only are called private members.
"""
# Private members:
# In Python, private members are accessible only within the class.
# They are not accessible from outside the class.
# The private members of a class are defined by prefixing the member name with double underscore “__”.

# Python program to demonstrate private members
# "__" double underscore represents private attribute.
# Private attributes start with "__".

# Creating a Base class
class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks2"

# Creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling constructor of Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c) # prints GeeksforGeeks2

    def access_private(self): # this method is used to access private member of base class
        # Accessing private member of class
        print("Accessing private member of base class: ")
        print(self.__c) # prints GeeksforGeeks2 without error

# Driver code
obj1 = Base() 
print(obj1.a) # prints GeeksforGeeks as it is public member
print(obj1.__c) # raises an AttributeError as it is private member
print(obj1._Base__c) # prints GeeksforGeeks2 as it is private member
print(obj1.access_private()) # prints GeeksforGeeks2 as it is internal function of class and has private member

# Public members:
# Members of a class that are accessible from anywhere are called public members.
# This is the most common type of access modifier.
# If we do not specify any access modifier, then by default the members are public.
# We can access the public members from outside the class using the dot (.) operator.

# Python program to demonstrate public members
# Creating a Base class
class Base:
    def __init__(self):
        # Declaring public variable
        self.b = "GeeksforGeeks"

# Creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling constructor of Base class
        Base.__init__(self)
        print("Public member of base class: ")
        print(self.b) # prints GeeksforGeeks

# Driver code
obj = Base()
print(obj.b) # prints GeeksforGeeks

# Protected members:
# Members of a class that are accessible from within the class and its subclasses are called protected members.
# In Python, protected members are those members that follow the naming convention as _<name>. (single underscore before the data member name)
# We can access the protected members from outside the class but only through inheritance.
# To access protected members, we can use the dot (.) operator with the object of the class.

# Python program to demonstrate protected members
# Creating a Base class
class Base:
    def __init__(self):
        # Protected member
        self._c = "GeeksforGeeks3" # protected member starts with single underscore

# Creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling constructor of Base class
        Base.__init__(self)
        print("Protected member of base class: ")
        print(self._c)

# Driver code
obj = Base()
print(obj._c) # prints GeeksforGeeks3 as it is protected member


"""
Private methods:
In Python, private methods are accessible only within the class.
They are not accessible from outside the class.
The private methods of a class are defined by prefixing the member name with double underscore “__”.
"""

# Python program to demonstrate private methods
# "__" double underscore represents private attribute.

# Creating a Base class
class Person:
    def __init__(self):
        self.a = "i am public"
        self.__c = "i am private"

    # private method
    def __display(self): 
        print("Private member of base class: ")
        print(self.__c)

    #public method to access private method
    def show(self):
        print("Public member of base class: ")
        print(self.a)
        self.__display()

p1= Person()
print(p1.a) # prints i am public
print(p1.__c) # raises an AttributeError as it is private member
#but we can access private member from using below syntax:
print(p1.show()) # prints i am private as public method is used to access private method

