def build_max_heap(A,i):
	largest = i
	l=(i*2)+1
	r=(i*2)+2
	if l<len(A):
		largest = max([(A[i],i),(A[l],l)])[1]
	if r<len(A):
		largest = max([(A[i],i),(A[r],r)])[1]
	if largest!=i:
		A[largest],A[i]=A[i],A[largest]
		build_max_heap(A,largest)
def heapify(A):
	for i in range(len(A)//2,-1,-1):
		build_max_heap(A,i)
	return A
print(heapify([9,1,23,4,2,10]))