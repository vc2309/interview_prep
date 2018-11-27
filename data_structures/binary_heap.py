class Heap(object):
	"""Class to represent a binary max heap implemented with an array"""
	def __init__(self):
		self.heap = [-float('inf')]
		self.heap_size = 0

	def swap(self,i,j):
		self.heap[i],self.heap[j]=self.heap[j],self.heap[i]
	def parent(self,i):
		return (i)//2
	def bubbleUp(self,i):
		parent = self.parent(i)
		while parent>0:
			if self.heap[parent]<self.heap[i]:
				self.swap(i,parent)
			i=parent
			parent=self.parent(i)
	def min_child(self,i):
		if i*2+1>self.heap_size:
			idx= (i*2)
		else:
			idx = (i*2) if self.heap[i*2]>self.heap[(i*2)+1] else ((i*2)+1)
		return idx
	def bubbleDown(self,i):
		while (i*2)<=self.heap_size:
			nxt=self.min_child(i)
			print(i,nxt)
			self.swap(i,nxt)
			
			i=nxt

			
	def insert(self,val):
		self.heap_size+=1
		self.heap.append(val)
		self.bubbleUp(self.heap_size)
		print(self.heap)

	def getMax(self):
		try:
			return self.heap[1]
		except IndexError as e:
			print("Empty heap")
	def deleteMax(self):
		max = self.getMax()
		if self.heap_size>1:
			self.heap[1]=self.heap[self.heap_size]
			self.heap_size-=1
			self.bubbleDown(1)
			self.heap.pop()
		return max


myHeap = Heap()
myHeap.insert(5)
myHeap.insert(9)
myHeap.insert(9)
myHeap.insert(10)
myHeap.insert(4)
myHeap.insert(11)
myHeap.insert(11)
myHeap.insert(11)
print(myHeap.getMax())
print(myHeap.deleteMax())
print(myHeap.heap)
myHeap.insert(113)
print(myHeap.deleteMax())

