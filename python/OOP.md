# Object Oriented Programming in Python
- We can see here how we achieve:
	1. Inheritance
	2. Data hiding (provate variable)
	3. Static variable
	4. Overloading the printing operator fxn
	5. Calling the super function
	
	```python
	class Base(object):
	    #This is how we declare a static variable
	    count=0
	    def __init__(self,val):
	        self.__val = val #How to make a private member
	        Base.count+=1
	    def get_val(self):
	        return (self.__val)
	    def get_count(self):
	        return (Base.count)
	    def __str__(self):
	        return self.get_val()
	class Derived(Base):
	    def __init__(self,key,val):
	        super().__init__(val)
	        self.__key = key
	    def get_key(self):
	        return self.__key
	    def __str__(self):
	        print(self.get_key(),end=" : ")
	        print(super().get_val())
	        return ""
	```
## Class method vs Static method
- Class methods use the @classmethod decorator and take *cls* which is the class, as a parameter. They can access the class state.
- Static methods don't take the params, and have no access to class state or instance state. They are usually utility functions.

## First Class Functions
Properties of first class functions:

A function is an instance of the Object type.
You can store the function in a variable.
You can pass the function as a parameter to another function.
You can return the function from a function.
You can store them in data structures such as hash tables, lists, …
