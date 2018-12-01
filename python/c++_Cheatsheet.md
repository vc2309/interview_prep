# C++ Cheatsheet

## 1. Coercion
- Reinterprets a value to another type (may not be meaningful)
	
	``` c++
	  int i, *ip = &i; // ip points to int i
	  double d, *dp = &d
	  dp = (double *) i; //points to an integer
	  // or
	  dp = reinterpet_cast<double *>(ip);
	```

## 2. Exception Handling
- We `throw Exception()` and it is handled by a handler subroutine which must `catch (Exception){...}`
- Handler can reraise, stop or raise another exception.
- <reraise> is done by using `throw` within the handler.

## 3. Type Constructor
- We use these to build complex types from basic types

### 3.1 Enumeration
- Type used to define a set of named literals with only assignment, comparison and conversion to integer.

	```c++
	enum Days = {Monday,Tuesday,Wednesday};
	Days d1 = Wednesday;
	```

### 3.2 Pointers/ references

- These are an address in memory

	```c++
	int x,y;
	int *p1 = &x, *p2=&y;
	```
- Pointer assignment vs value assignment

	```c++
	p1 = p2 // now p1 points at y.
	//instead if we do
	*p2 = *p1 // now value of y is equal to value of x
	```
- Using reference pointer instead

	```c++
	int &p1 = x;
	//p1 is the value 
	int & (&rr) = r; // reference to reference, rewritten &r
	int &(*p1) = &r; // pointer to reference
	```

### 3.3 Arrays

```int arr[10];```

- Arrays are continguous in memory

	```c++
	int i, arr[10];
	int *parr = arr; // think parr[], pointer to array of N ints
	```

### 3.4 Structs

- Collection of heterogenous values
- Can also have functions
- <all members are public by default>

`struct Complex {double re, im} c;` One line declaration

- Dereferencing

	```c++
	(*sp1).name is the same as sp1->name
	```

### 3.5 Memory Management
- unmanaged language -> the programmer must take care of this

#### new keyword
- used to allocate HEAP memory for an object
- 3 steps:
	1. determine size
	2. allocate heap storage of correct size
	3. coerce undegined storage to correct type

#### delete keyword
- used to free space from heap
- delete must be used with a reference or a pointer

	```c++
	Foo *p = new Foo;
	...
	delete p;
	```
- deleting array
`int *parr = new int[10]; delete [] parr;`


### 3.6 Namespaces
- C++ namespaces are used to organize libraries and programs of multiple types and declarations to deal with name conflicts
- namespace std contains IO declarations
- 

	```c++
	namespace Foo { int i = 0; } namespace Bar { int i = 1; } 
	{
		int i = 2;
		using namespace Foo; // i exists in scope, alias ignored }
	{
	using namespace Foo;
	using namespace Bar; // i exists from using directive i = 0; // conflict failure, ambiguous reference to ’i’
	}
	```


#### Dynamic allocation should be used only when a variable’s storage must outlive the block in which it is allocated (see also page 103).

### 3.7 Routines and Memory

- each routine or function calls a new block or frame on the stack
- any allocated memory is in the heap
- static variables and global variables are stored in static memory
- parameters of functions are stored in their stack frame
- unintialized local variables are stored in the stack

#### 3.7.1 Passing by reference or value
- In c++ we can do either
- If its a value param, the copy is stored in the routines block on the stack(may have implicit conversion)
- reference params have their address pushed on the stack and this is referenced to get the value
- Good practise uses reference parameters rather than pointer.
- *Arrays are always passed by reference* `double sum( double *m[] );`

#### 3.7.2 Overloading
- Giving multiple functions the same name to allow varied functionality based on argument type/number

### 3.8 Object Oriented Programming
- Based on structures to organize logically related data
- An object provides both data and the operations necessary to manipulate that data in one self-contained package.

##### Interface:
- Interface separates usage from implementation at the interface boundary,
- Developing good interfaces for objects is important.

#### Object members
- Structures/classes have their own scope for each instance
- Structure scope is implemented via a T * const this parameter, implicitly passed to each routine member (like left example).

	```c++
double abs() const {
return sqrt( this->re * this->re + this->im * this->im ); }
```

- Since implicit parameter “this” is a const pointer, it should be a reference.

#### Operator members
- These are functions called using symbols on the instance variables.

	```c++
Complex operator+( Complex c ) { // rename add member return { re + c.re, im + c.im };
}
```

#### Constructor
- Implicitly performs initialization after object allocation to ensure the object is valid for use
- For dynamic allocation,constructor arguments after type:
	```c++
Complex *x = new Complex; // x->Complex();
Complex *y = new Complex( 3.2, 4.5 ); // y->Complex( 3.2, 4.5 ); Complex *z = new Complex{ 3.2 }; // z->Complex( 3.2 );
	```

#### Literals
- Constructors are used to create object literals as well

	```c++
Complex x,y,z;
x = {3.2};
y = x + (Complex){3.2,4.5};
}
	```

#### Conversion
	```c++
	int i;
	double d; Complex x, y;
	x = 3.2;
	y = x + 1.3; y = x + i;
	y = x + d;
	implicitly rewritten as
	x = Complex( 3.2 );
	y = x.operator+( Complex(1.3) );
	y = x.operator+( Complex( (double)i ); y = x.operator+( Complex( d ) );
	```
- We can turn off these implicit conversions by using `explicit` in unction definition.

#### Destructor
- Destructor is ONLY REQUIRED when an object has members which are non contingously stored and dynamically allocated.
- Contiguous objects are not needed to have a destructor
- Destructor is called before deallocation either implicitly or explicitly by using `delete`
- Destructors must be called in reverse order to constructors because of dependencies.

#### Destructor is implicitly noexcept
- Destructors can raise exceptions if the inherit from a class having noexcept(false)
- If we raise exception in destructor, then on propagation aka handling another error, if the destructor is called, we cannot handle the exception thrown by the destructor, because the previous exception is still being handled. Program terminates.

#### Copy Constructor / Assignment Operator

-  Constructor with a const reference parameter of class type is used for initialization (decla- rations/parameters/return), called copy constructor:
`Complex( const Complex &c ) { ... }`

- Assignment operator `Complex &operator=( const Complex &rhs ) { ... }`
- If a copy constructor or assignment operator isnt defined,an implicitone is generated that does a memberwise copy of each subobject.

#### Initialize const / Object Member
- C/C++ const members and local objects of a structure must be initialized at declaration:

### 3.8.1 Encapsulation
- Putting all implementation within object and hides it to support abstraction.



#### Scopes
- public/private/protected visibility
- friendship : Mechanism to allow outside routines (non member) to access private variables.

#### Pipml pattern : Used to completely hide the implementation of a class
- Create a class `Complex`, within which you create a struct called `ComplexImpl`, within which you do the actual implementation.
- Create a reference to a `ComplexImpl` object called `ComplexImpl &impl` which is a member of the Complex class.
- Now you can use the functions and memebers of `impl` to carry out all the operations in `Complex`.

### 3.8.2 Inheritance
- Re-using logic for related classes
- Implementation inheritance provides reuse of code inside an object type.
- Type inheritance provides reuse outside the object type by allowing existing code to access the base type.

#### Implementation Inheritance (Has - a)
- Composition is Implicit (car has-a engine)

	```c++
	struct Engine { // Base int cyls;
	int r(...) { ... }
	Engine() { ... } };
	struct Car : public Engine { // implicit // composition
	int s(...) { cyls = 4; r(...); ... }
	Car() { ... } } vw;
	vw.cyls = 3; // direct reference vw.r(...); // direct reference vw.s(...); // direct reference
	```

- Instead of making `Engine` owned by `Car`, we can extend `Engine` with more features to make it a `Car` and make `Car` inherit from `Engine`.

#### Type Inheritance (is - a)

- Making a base type from which more detailed sub types can be extended.

	```c++
	class Employee{
		//...
	}
	class PartTime:public Employee{
		//...
	}
	```
- We have name equivalence here so we can allow routines to handle multiple types called polymorphism.
- **Type inheritance relaxes name equivalence by aliasing the derived name with its base type names**

##### Example of using Type and Implementation inheritance
	
	```c++
	class Complex{//..}
	class MyComp : public Complex {
		int cntCalls;
		MyComp(double re,double im=0.0) : Complex(re,im) , cntCalls(0) {}

		double abs(){ 	//override
			cntCalls+=1;
			return Complex::abs(); //Using the implementation of Complex 
		}
		int calls() { return cntCalls;} 
	}
	```
#### Contravariance
- One problem with type inheritance and name equivalance is this:
- for overloading operator +, we have `Complex &operator(Complex,Complex)` , which cant take in subtypes of Complex, but will return a Complex only.
- Hence if we assign the result of this operation to a MyComp, it will not have the cntCalls member.

### Constructor/ Destructors
- Constructors are executed top down, destructors in opposite order

	```c++
	class Derived: public Base{
		Derived(int x): Base(x), cnt(0) {}
		~Derived(){} // ~Base is implicitly called
	};
	```

### Copy Constructor/Assignment
- How to implement copy constructor/assignment with inheritance

	```c++
	class B{
		int i;
		public:
		B(int i) : i{i} {}
		B(const B& other) : i{other.i} {}
		B &operator=(const B& other) {
			i = other.i;
			return *this;
		}
	};
	class D: public B{
		int j;
		public:
		D(int j): j{j} {}
		D(const &D other) : B(other), j{other.j} {}
		D &operator=(const &D other) {
			(B &)*this = other; //coercion
			j = other.j;
			return *this;
		}
	};
	```

### Overloading
- Overloaded routines in subclasses override the base class routines.
- We can still access base class members like this `Base::routine()`

### Virtual Routines
- When you call a routine from a pointer/reference to a derived object, it will call the base routine if it is interpreted as a Base class pointer.
- To invoke a routine defined in a referenced object, qualify the member routine with `virtual`. To invoke the routine which is defined by the **type** of a pointer/reference, don't use virtual
- So if you have an object which is of type `Derived1`, and another of `Derived2`, and they are both referenced by a `Base` pointer, used `virtual` to access a special implementation of any routine, but to use the `Base` implementation, dont use `virtual`.
- Java always uses virtual for all calls to objects
- Once a base type qualifies a routine member as virtual, it is virtual for all derived types.
- **Virtual members are only necessary to access derived members through base type reference or pointer**
- **Any type with virtual members needs to make the destructor virtual (even if empty) so the most derived destructor is called through a base-type pointer/reference.**

##### Polymorphic Assignment	
- How to manipulate polymorphic references
	```c++
	struct Base {
		void f() {} // non-virtual 
		void g() {} // non-virtual 
		virtual void h() {} // virtual
		};
	struct Derived : public Base {
		void g() {};
		void h() {}; 
		void e() {};
	};
		Base &b = new Derived();
		b.f() // calls Base::f()
		(Derived  &)b.g() // calls explicitly Derived::g()
		b.Base::h() // explicit call to Base::h()
		b.h() // Derived::h()
	```

### Dynamic cast
- determines the base type of a derived reference

	```c++
	Base *bp = new Derived;
	Derived *dp;
	dp = dynamic_cast<Derived *>(bp);
	if dp(!=0){//it is derived}
	```

- The type must have at least one virtual member

### Slicing
- polymorphic copy/assignment can result in object truncation clled slicing.

### Protected members
- Protected members are accessible by inherited classes of base classes.

### Abstract Classes
- Combines Implementation and Type in heritance for ***structuring new classes***
- Contains **at least 1 pure virtual member** which is implemented by derived classes

	```c++
	class Shape{
		enum Colour{Red, Black, White} c;
		public:
			virtual void move(int x,int y) = 0; //this is how to declare pure virtual
	}
	```

- Provide (pure) virtual member to allow overriding and **force implementation by derived
class.**
- Non-virtual routines are provided to *force base implementation*, rest must be implemented by the concrete classes.
- **Concrete class** inherits from one or more abstract classes and defines all pure virtual functions.
- You ***cannot instantiate* an abstract class but can *declare reference or pointer* of it** 