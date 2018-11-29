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