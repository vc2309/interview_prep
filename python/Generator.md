# Generators
- Generators are functions which use the yield keyword as an exit point also used to return values. Each time a generator is called, it enters after the last yield expression.
	
```python
	def xrange_(lower=None,upper=None,step=1):
		if lower==None and upper==None:
			raise KeyError
		elif upper==None:
			lower, upper = 0, lower
		while lower<upper:
			yield lower
			lower+=step
```

## Using the generator as a function
	
```python	
	for i in xrange_(10):
		print(i)
```

## Using the generator as an object

```python
	#we can get an iterator object from the generator function
	iterator = xrange_.__iter__()
	while True:
		try:
			print(next(iterator))
		except:
			break
```

Difference between Generator function and Normal function –

Once the function yields, the function is paused and the control is transferred to the caller.
When the function terminates, StopIteration is raised automatically on further calls.
Local variables and their states are remembered between successive calls.
Generator function contains one or more yield statement instead of return statement.
As the methods like _next_() and _iter_() are implemented automatically, we can iterate through the items using next().

## Generator Expression
- We can make lists with list comprehensions like
a = [i for i in range(2,41)]

- Similarly generator expression is like
gen = (num ** 2 for num in range(10))
