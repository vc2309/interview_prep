# Hashing

## Dictionary
- Insert, delete search
- Inefficient to use a linked list : O(n) searching/deleting

## Hashing
- Idea consists of
1. A table of size 0-m which stores the elements
2. A hash function which takes a key k and returns a number from 0-m which is the index of the element in the hash table.

## Collisions
- When two keys have the same hash value, they have a collision which means they are required to be stored in the same index of the hash table.
- How to handle this:
1. Good hash function which minimizes collisions
2. Collision resolution strategy

## Open hashing / Chaining
- In this strategy, we maintain pointers at each index of the hash table
- Any time we have a collision, we simply add a new node at the index pointer given by h(k)

### Chaining analysis
- **load factor *a*** : `a=n/m` where m is total slots and n is total elements.
- **Insert** : O(1)
- **Delete/Search** : O(n)

### Simple uniform hashing
- Performance depends on the hash function
- A good hash function should:
	1. Have an equal probability of returning all m indices
	2. Be easy to compute

#### Multiplication method
1. Pick a constant 0<A<1
2. Take fractional part of k\*A
3. y=frac(k\*A)\*m
4. z=int(y)
5. h(k) = z
- A should generally be an irrational

## Open addressing / Closed hashing
- No linked list, only hash table
- each entry is either an element or NIL
- Saves memory(no pointers) and time(alloc/dealloc)

### Collision resolution
- Probing
- If we have a collision with h(k), we use our probe sequence with function h(k,i) with i being the number of collisions
- `h(k,i) = [h(k)+f(i)] mod m`
- f(0)=0 is a must

### Algos
- Insert O(n) worst case

	```pseudocode
	insert(T,elem):
		i=0
		k=elem.key
		do:
			j = h(k,i)
			if T[j]!=NIL:
				i+=1
				continue
			else:
				T[i]=elem
		while i<m
	```
- Search O(n) worst case
	```pseudocode
	search(T,k):
		i=0
		do:
			j = h(k,i)
			if T[j].key == k:
				return j
			i+=1
		while T[j]!=NIL and i<m
	```
