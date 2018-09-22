def perm(string,idx):
	
	if idx==1:
		a=string[idx]
		b=string[idx-1]
		my_perms=[a+b,b+a]
	else:
		char = string[idx]
		curr_perms = perm(string,idx-1)
		my_perms=[]
		for pmt in curr_perms:
			for pos in range(len(pmt)+1):
				my_perms.append(pmt[:pos]+char+pmt[pos:])
	return my_perms

def get_perm(string):
	if len(string)<2:
		return string
	return perm(string,len(string)-1)

print len(get_perm("hello"))
	

