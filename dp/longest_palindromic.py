def max_len(string,start,end):
	
	if start>end:
		return 0
	elif start==end:
		return 1
	if string[start]==string[end]:
		return 2+max_len(string,start+1,end-1)
	else:
		return max(max_len(string,start+1,end),max_len(string,start,end-1))

string="BBABCBCAB"
print(max_len(string,0,len(string)-1))