# Destructor: 
# -- Destructor is a special method that is called when an object is destroyed.
# -- It is called when the reference count becomes zero.
# -- It is also called the garbage collector.
# -- Destructor is used to clean up the resources.

# -- Destructor is defined using __del__() method.
# -- Syntax: def __del__(self):
# -- Destructor is called when the object is destroyed.

# Example:
class Test:
    def __init__(self):
        print("Object Initialization")
    def __del__(self):
        print("Destructor Invoked")

t1 = Test() # Reference count is 1 , t1 is pointing to Test object
t2 = t1 # Reference count is 2 , t2 is pointing to t1 because of this reference count is 2
t3 = t1 # Reference count is 3  , t3 is pointing to t1 because of this reference count is 3
del t1 # Reference count is 2 , destructor is not called as reference count is not zero
del t2 # Reference count is 1 , destructor is not called as reference count is not zero
del t3 # Reference count is 0 , now destructor is called as reference count is zero

# Output:
# Object Initialization
# Destructor Invoked

# Note:
# --object is created using __new__() method and initialized using __init__() method.
# --object is destroyed using __del__() method.

#Advantages of Destructor:
# -- It is used to release the resources.
# -- It is used to perform clean up activities.
# -- It is used to perform clean up activities before the object is destroyed.

# Disadvantages of Destructor:
# -- It is not recommended to use destructor because it is not guaranteed that when the destructor will be called.
# -- It is not recommended to use destructor because it is not recommended to use garbage collector.
# --Circular Reference: If two objects are referring to each other then the reference count will never become zero and the destructor will never be called.
# Exception in __init__(): If an exception is raised in __init__() method then the object is not created and the destructor is not called.

#example of circular reference:
class A:
    def __init__(self):
        print("Object Initialization")
        self.b = B(self)
    def __del__(self):
        print("Destructor Invoked")

class B:
    def __init__(self,a):
        print("Object Initialization")
        self.a = a
    def __del__(self):
        print("Destructor Invoked")

a = A() # Reference count is 1 , a is pointing to A object and A object is pointing to B object and B object is pointing to A object so reference count is not zero and destructor is not called.

# Output:
# Object Initialization
# Object Initialization

# in above output, destructor is not called because of circular reference.


# Example of exception in __init__():
class Test:
    def __init__(self):
        print("Object Initialization")
        raise ZeroDivisionError
    def __del__(self):
        print("Destructor Invoked")

t1 = Test() # Exception is raised in __init__() method so object is not created and destructor is not called.

# Output:
    # Object Initialization
    # Traceback (most recent call last):
    #   File "Destructor.py", line 47, in <module>
    #     t1 = Test()
    #   File "Destructor.py", line 45, in __init__
    #     raise ZeroDivisionError
    # ZeroDivisionError

