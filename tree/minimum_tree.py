from bst import Tree,Node

def minimum_tree(my_arr,my_tree,l,r):
	if l<r:
		mid = int((l+r)/2)
		my_tree.insert(my_arr[mid])
		minimum_tree(my_arr,my_tree,l,mid-1)
		minimum_tree(my_arr,my_tree,mid+1,r)
	if l==r:
		my_tree.insert(my_arr[l])

def main():
	my_arr = [int(i) for i in input("enter nums").split(' ') if i!='']
	my_tree=Tree()
	minimum_tree(my_arr,my_tree,0,len(my_arr)-1)

if __name__ == '__main__':
	main()