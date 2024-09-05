"""
Operator Overloading:
Python operators work for built-in classes.
But the same operator behaves differently with different types.
For example, the + operator will perform arithmetic addition on two numbers, merge two lists, or concatenate two strings.
This feature in Python that allows the same operator to have different meanings is called operator overloading.
"""

# Operator & dunder methods:
# a+b  (equals to) = a.__add__(b)
# a-b  (equals to) = a.__sub__(b)
# a*b  (equals to) = a.__mul__(b)
# a/b  (equals to) = a.__truediv__(b)
# a//b (equals to) = a.__floordiv__(b)
# a%b  (equals to) = a.__mod__(b)
# a**b (equals to) = a.__pow__(b)
# -a   (equals to) = a.__neg__()
# +a   (equals to) = a.__pos__()
# a==b (equals to) = a.__eq__(b)
# a!=b (equals to) = a.__ne__(b)

# For example, the + operator will perform arithmetic addition on two numbers, merge two lists, or concatenate two strings.
print(1+2) # Output: 3 , adding two numbers
print('a'+'b') # Output: ab, concatenating two strings
print([1,2]+[3,4]) # Output: [1, 2, 3, 4], merging two lists


"""but for complex numbers, + will behave differently, so use dunder methods to overload the operator
#use __add__ dunder method to overload the + operator"""

class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __add__(self, other): #dunder method to overload the + operator
        return Complex(self.a + other.a, self.b + other.b)
    
    def __str__(self):
        return f'{self.a} + {self.b}j'
    
c1 = Complex(1, 2)
c2 = Complex(2, 3)
c3 = c1 + c2 #this runs because of the dunder method __add__ else gives error
print(c3) # Output: 3 + 5j

