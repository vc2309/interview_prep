class Node(object):
	"""docstring for Node"""
	def __init__(self):
		self.ele=None
		self.left=None
		self.right=None
		self.parent=None

class Tree(object):
	"""docstring for Tree"""
	def __init__(self):
		self.root=Node()

	def insert(self,val):
		print(val)
		self.insertUtil(val,self.root)

	def insertUtil(self,val,root):
		if root.ele==None:
			root.ele=val
		else:
			if root.ele<val:
				if root.right:
					self.insertUtil(val,root.right)
				else:
					root.right=Node()
					root.right.ele=val
					root.right.parent=root
			elif root.ele>val:
				if root.left:
					self.insertUtil(val,root.left)
				else:
					root.left=Node()
					root.left.ele=val
					root.left.parent=root
			else:
				print("Already exists")

	def search(self,val,root):
		if root==None:
			print("Not found")
		elif root.ele>val:
			res=self.search(val,root.left)
		elif root.ele<val:
			res=self.search(val,root.right)
		else:
			print("here {}".format(root.ele))
			print(type(root))
			return root
		return res

	def minTree(self,root):
		cur=root
		while root.left!=None:
			root=root.left
		return root

	def maxTree(self,root):
		cur=root
		while root.right!=None:
			root=root.right
		return root

	def successor(self,val):
		x=self.search(val,self.root)
		print(type(x))
		if x.right==None:
			y=x.parent
			while y and x==y.right:
				x=y
				y=x.parent
			if y:
				print(y.ele)
			else:
				print("this is the greatest element")

		else:
			print(self.minTree(root.right))

	def predecessor(self,val):
		x=self.search(val,self.root)
		print(type(x))
		if x.left:
			print(x.left.ele)
		else:
			y=x.parent
			# print(y.ele)
			while y and x==y.left:
				x=y
				y=y.parent
			if y:
				print(y.ele)
			else:
				print("this is the greatest element")

	def delete(self,val):
		z=self.search(val,self.root)
		if (not z.left) or (not z.right):
			y=z
		else:
			y=self.minTree(z.right)
			z.ele=y.ele
			z.right=y.right
			z.left=y.left

		if y.left:
			x=y.left
		else:
			x=y.right

		if y==y.parent.left:
			y.parent.left=x
			x.parent=y.parent
		else:
			y.parent.right=x
			x.parent=y.parent

	def print(self,root):
		if not root:
			return
		else:
			self.print(root.left)
			print(root.ele)
			self.print(root.right)


def main():
	t=Tree()
	nodes=[5,4,2,3,1,7,8,9,6,10]
	for n in nodes:
		t.insert(n)
	ch=-1
	while ch!=0:
	 	ch=int(input("{} : max \n{} : min \n{} : search \n{} : successor\n{} : predecessor\n{} print\n{} delete\n{} input\n".format(1,2,3,4,5,6,7,8)))
	 	if ch==1:
	 		print((t.maxTree(t.root)).ele)
	 	elif ch==2:
	 		print((t.minTree(t.root)).ele)
	 	elif ch==3:
	 		val=int(input("Input the value to search\n"))
	 		r=t.search(val,t.root)
	 		if r!=None:
	 			print(r.ele)
	 	elif ch==4:
	 		val=int(input("Input the value to get successor of\n"))
	 		t.successor(val)

	 	elif ch==5:
	 		val=int(input("Input the value to get predecessor of\n"))
	 		t.predecessor(val)

	 	elif ch==6:
	 		t.print(t.root)

	 	elif ch==7:
	 		val=int(input("Input the value to delete\n"))
	 		t.delete(val)

	 	elif ch==8:
	 		val=int(input("Input the value to insert\n"))
	 		t.insert(val)
	 		

if __name__ == '__main__':
	main()
		
					


		