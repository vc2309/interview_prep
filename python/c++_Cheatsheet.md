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
• C/C++constmembersandlocalobjectsofastructuremustbeinitializedatdeclaration:

### 3.8.1 Encapsulation
- Putting all implementation within object and hides it to support abstraction.

#### Scopes
- public/private/protected visibility
- friendship : Mechanism to allow outside routines (non member) to access private variables.

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

- 

