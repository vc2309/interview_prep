# Variables in python

## Global vs Local

- Local variables

		def fn():
			s="ok"
			print(s)
		s="no"
		fn()

- Output : "ok"

- However, in the case that we have an assignment within the function, we must use the global keyword

		def fn():
			global s
			print(s)
			s="yes"
			print(s)

		global s
		s="no"
		fn()
- Output: "no"
          "yes"

- We can also assign global variables within functions
		```
		def fn():
		   ...:     global s
		   ...:     print(s)
		   ...:     s="yes"
		   ...:     global ss
		   ...:     ss="noooo"
		   ...:     print(s)
		   ...: 
		   ...: s="no"
		   ...: fn()
		   ...: print(ss)
		   ...: 
		```
no
yes
noooo


## Unpacking/Packing values
Ways to unpack list and tuple:

1. arr = [1,2,3,4]
	a,b,c,d = arr

	or

	def fn(a,b,c,d):
		pass
	fn(\*arr)

If we want to accept a packed number of variables into a function

		def fxn(*args):
            args = list(args)
            args = [i*2 for i in args]
            print(args)
        fxn(a,b,c,d)

[2, 4, 6, 8]

2. \*\*kwargs for dicts

		def fxn(**kwargs):
			for key in kwargs:
				print(key,kwargs[key])

		fxn(a=23,b=34,l=9)