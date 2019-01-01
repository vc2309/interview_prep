# HashMap

## Operations
1. Insert
2. Search
3. Delete

## Hashing
1. Table (array of size `m` which maintains values)
2. Hash function (hashes a key `k` to an address in the array between `[0..m]`)

## Collisions
- A collision is when two keys hash to the same address.
- Strategies to avoid collisions:
	1. Chaining (open hashing)
	2. Open addressing / Closed chaining

## Chaining
- Maintain m element array with m pointers.
- Each cell in the array points to a linked list
- When there is a collision just add the new element to the front of the list
- Load factor = `a = n/m` where m is size of array and n is no. of elements.

### Complexity
- Insert O(1)
- Search O(a) if we have **Simple uniform hashing** else O(n)
- Delete O(a) if we have **Simple uniform hashing** else O(n)

### Hash functions
1. **Division method**
- ` h(x) = m mod x`
- Choosing m
	- Not a power of 2
	- Not a power of 10
	- Prime number
2. **Multiplication method**
- ` h(x) = int(frac(x*A) * m)` WHERE 0<A<1
- Choosing A
	- Irrational number (1-sqrt(2))

## Closed hashing
- No chaining only 1 element per table
- Why?
	- Constant complexity always
	- Less memory usage (we can store more elements with the same memory)
- Collision strategy : 
	- Probing function `f(i)`
	- `h'(k,i) = [h(k)+f(i)] mod m`
	- Increment i each time we hit a collision
- Insert algorithm:
	- Wile `(i<m)`
	- Calculate `h'(k,i)`
	- If 'NIL' or 'DELETED', insert (k,v)
	- else i++
- Search algo:
	- While `(i<m)`
	- Calculate `h'(k,i)`
	- If you hit NIL -> element doesnt exist
	- else if the element at this index has the same key as the searched key, return value
	- else i++
- Delete
	- Same as search except delete

### Complexity
- Load factor should be below 0.5
- **Rehash** if the load factor is above 0,5, double the size of the table and rehash