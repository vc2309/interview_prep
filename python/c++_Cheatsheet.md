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
- 