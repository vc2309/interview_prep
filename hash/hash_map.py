import numpy as np
class Hash_Table(object):
	"""docstring for Hash_Table"""
	def __init__(self):
		self.size=100
		self.table=[None for i in range(self.size)]

	def choice(self,ch):
		if ch==1:
			k=input("Enter key\n")
			v=int(input("Entr val\n"))
			self.add(k,v)
		elif ch==2:
			k=input("Enter key\n")
			res=self.search(k)
			if res:
				print("Value is {}".format(res))
			else:
				print("Not found!")
		else:
			k=input("Enter key\n")
			self.delete(k)
		return


	def hash_fxn(self,key):
		k=0
		for c in key:
			k+=ord(c)

		A=(22/7)-3
		prod=A*k
		print(prod)
		frac=prod-int(prod)
		print(frac)
		result=(int((frac)*self.size)%self.size)
		print(result)
		return result

	def delete(self,key):
		i=self.hash_fxn(key)
		if self.table[i]:
			for k,j in enumerate(self.table[i]):
				if j[0]==key:
					del(self.table[i][j])
					
		else:
			print("Not exists")


	def add(self,key,val):
		i=self.hash_fxn(key)
		if self.table[i]==None:
			self.table[i]=[]
			self.table[i].append((key,val))
		else:
			self.table[i].append((key,val))

	def search(self,key):
		i=self.hash_fxn(key)
		if self.table[i]==None:
			return None
		else:
			for j in self.table[i]:
				if j[0]==key:
					return j[1]
					

def main():
	ch=-1
	ht=Hash_Table()
	while ch!=0:
		ch=int(input("1 to Add, 2 to Search, 3 to delete, 0 to quit\n"))
		if ch>0:
			ht.choice(ch)

if __name__ == '__main__':
	main()



		
		