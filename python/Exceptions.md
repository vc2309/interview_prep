# Exception Handling

## Try and Except

	```python
	try:  
	    print "Second element = %d" %(a[1]) 
	  
	    # Throws error since there are only 3 elements in array 
	    print "Fourth element = %d" %(a[3])  
	  
	except IndexError: 
	    print "An error occurred"
	```

## Try, except and else
- The else clause is entered if try does not raise an exception

	```python
	def AbyB(a , b): 
	    try: 
	        c = ((a+b) / (a-b)) 
	    except ZeroDivisionError: 
	        print "a/b result in 0"
	    else: 
	        print c 
	```

## Raising Exceptions

` raise NameError("hi")`

## User defined exceptions
- Must derive Exception class
- Should have a \__str__ fxn