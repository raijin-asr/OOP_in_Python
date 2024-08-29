# Methods are functions that belong to objects.
#creating class
class Student: 
    def __init__(self, fullname ):
        self.name =  fullname
        
    def hello( self ): #method with self as parameter
        print("Hello", self.name)
       
#creating object to access methods
s1 =  Student("Ram") #creating object of Student class
s1.hello( ) #calling method using object
# Output: Hello Ram


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

# @classmethod:
# A class method is a method that is bound to the class and not the object of the class.
# They have the access to the state of the class as it takes

class EmployeeY:
    company = "Google"
    def __init__(self, fullname):
        self.name =  fullname #object attribute > class attribute
    
    @classmethod #decorator to make it class method
    def hello(cls):
        print("hello", cls.company)

 #creating object
e2 =  EmployeeY("Ram" )
e2.hello() # Output: hello Google

# *The cls parameter is a reference to the current class, and is used to access class variables.
# *Class methods can be called by both class and object. But calling by class is preferred.
# *Class methods can access and modify class state.
# *Class methods can’t access or modify object state.
# *Class methods are bound to the class, not the object of the class.
# *Class methods are defined using a decorator @classmethod.
