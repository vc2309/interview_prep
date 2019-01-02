# Decorators

- We use decorator functions to take a function as an argument and return a function.
	
	```python
		def twice(fn):
			def do_twice():
				fn()
				fn()
			return do_twice
		@twice
		def site(s):
			print("ok",s)
	```

- in python, functions are *first class objects* which means that they can be referenced which means they can be *passed to a variable* and *returned by other functions*.

- Decorator allows us to use the behaviour of a function and *reuse it by modification*

- *_Decorators allow us to wrap another function in order to extend the behavior of wrapped function, without permanently modifying it._*

- What essentially happens here is:
	1. When we call site("ok"), we are actually doing this:
	```python
		site = twice(site("ok"))
		site()
	```
