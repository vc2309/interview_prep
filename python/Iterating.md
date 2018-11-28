# Iterable vs Iterator

- An iterable will produce and iterator when passed to iter() function.
	```python	
	iterator = iter(arr) # equivalent to arr.__iter__()
	while True:
		print(iterator.__next__()) # equivalent to next(iterator)
	```
- Iterators also are iterables. So iterator has __iter__() function as well.

