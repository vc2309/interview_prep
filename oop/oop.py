""" Demo of how to make use of OOP principles using Python """
"""
	In Python, class members are public except private variables, and all member functions are virtual. 
	Member functions are declared with 'self' to represent object. In function calls, this is implicit.
	We can also have operator overloading, just as in C++ 

"""

class Employee(object):
	"""docstring for Employee - this can be accessed through Employee.__doc__"""
	no_emps=0 #this is a CLASS VARIABLE - it is the same for all instances of this class
	def __init__(self, name, salary):
		Employee.no_emps+=1
		self.name =name
		self.salary=salary

	def displayCount(self):
		print("Total no. of Employees is {}".format(Employee.no_emps))

	def display(self):
		print("Name: {}\t Salary: {}\t".format(self.name,self.salary))

	"""
		NOTE: special functions to use on objects:
			getattr(obj, attr) - get value of obj.attr
			hasattr(obj,attr) - check if obj has an attribute 'attr'
			setattr(obj,attr,val) - setter
			delattr(obj,attr) - delete 

			"""	

	""" Operator overloading - as in C++ - python takes away a lot of overhead in terms of the syntax """
	def __lt__(self,emp):
		if hasattr(emp,'salary'):
			return self.salary<emp.salary
	def __gt__(self,emp):
		if hasattr(emp,'salary'):
			return self.salary>emp.salary
	def __eq__(self,emp):
		if hasattr(emp,'salary'):
			return self.salary==emp.salary




class Intern(Employee):
	"""docstring for Intern"""
	no_emps=0
	def __init__(self, name,salary,division):
		super(Intern, self).__init__(name,salary)
		self.division = division
		self.__private_string="Not for outsiders" #This is how to declare private variables in python classes. Start variable name with double underscore.
		Intern.no_emps+=1

	def displayCount(self):
		print("Total no. of Interns is {}".format(Intern.no_emps))

	def display(self):
		print("Name: {}\t Salary: {}\t division:{}".format(self.name,self.salary,self.division))

	def showPrivate(self):
		print(self.__private_string) #Since this is a member function, this will print the private variable


e1=Employee("Rohit",120)
e1.display()
e2=Employee("Ronak",130)
e2.display()

e1.displayCount()

i1=Intern("Vishnu",19000,"IT")
i1.display()
i1.displayCount()
e1.displayCount()
print(e1>i1)
print(i1==e2)
print(e2<i1)
i1.showPrivate()
try:
	print(i1.__private_string) #This will fail
except AttributeError:
	print("Private variable- cannot access")
	
"""
####
Output
####
Name: Rohit	 Salary: 120	
Name: Ronak	 Salary: 130	
Total no. of Employees is 2
Name: Vishnu	 Salary: 19000	 division:IT
Total no. of Interns is 1
Total no. of Employees is 3
False
False
True
Not for outsiders
Private variable- cannot access


"""




		