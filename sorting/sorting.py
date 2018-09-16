def selection(a):
	for i in range(len(a)):
		min_pos = i
		for j in range(i,len(a)):
			if a[j]<a[min_pos]:
				min_pos=j
		temp = a[i]
		a[i] = a[min_pos]
		a[min_pos] = temp

	return a

def bubble(a):
	for i in range(len(a)):
		for j in range(len(a)-i-1):
			if a[j]>a[j+1]:
				t = a[j]
				a[j]=a[j+1]
				a[j+1]=t
			print(a)
	return a			 	 

def merge(arr,l,midpoint,r):

	n1 = midpoint - l + 1
	n2 = r- midpoint -1
	print(l,midpoint,r)
	# create temp arrays 
	left = [0] * (n1) 
	right = [0] * (n2) 
    
	# Copy data to temp arrays L[] and R[] 
	for i in range(n1): 
		left[i] = arr[l + i] 

	for j in range(n2): 
		right[j] = arr[midpoint + 1 + j]

	ctr=l
	print(l,midpoint,r)
	print(left,right)
	while len(left) and len(right):
		elem=right.pop(0) if right[0]<left[0] else left.pop(0)
		arr[ctr]=elem
		ctr+=1
	while len(left):
		elem=left.pop(0)
		arr[ctr]=elem
		ctr+=1
	while len(right):
		elem=right.pop(0)
		arr[ctr]=elem
		ctr+=1
	print(arr)
def mergeSort(arr,l,r):
	print(l,r)
	if l<r:
		midpoint=int((l+(r-1))/2)
		mergeSort(arr,l,midpoint)
		mergeSort(arr,midpoint+1,r)
		merge(arr,l,midpoint,r)

def partition(arr,low,high):

	pivot = arr[high]
	left_pos = low - 1

	for i in range(low,high):
		if arr[i]<=pivot:
			left_pos+=1
			arr[i],arr[left_pos]=arr[left_pos],arr[i]
	arr[left_pos+1],arr[high]=arr[high],arr[left_pos+1]
	return left_pos+1

def quickSort(arr,low,high):
	if low<high:
		pi = partition(arr,low,high)
		quickSort(arr,low,pi-1)
		quickSort(arr,pi+1,high)

def main():
	a = [64 ,25 ,12 ,22, 11]
	print("Selection sort",selection(a))
	a = [64 ,25 ,12 ,22, 11]
	print("bubble sort",bubble(a))
	a = [12, 11, 13, 5, 6, 7]
	print("mergesort",mergeSort(a,0,len(a)))
	print(a)
	quickSort(a,0,len(a)-1)
	print("quicksort",a)


if __name__ == '__main__':
	main()