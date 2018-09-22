def check_perm(big_dict,count_dict):
	for a in big_dict.keys():
		if big_dict[a]!=count_dict[a]:
			return False
	return True

def get_all_perms(s,b):
	#window size
	w_len = len(s)
	count_dict = {char:0 for char in s}
	for char in s:
		count_dict[char]+=1

	start=0
	end=len(s)-1

	big_dict = {char:0 for char in s}
	
	for i in range(w_len):
		if big_dict.get(b[i])!=None:
			big_dict[b[i]]+=1
	# print(count_dict,big_dict)
	while end<len(b):
		if check_perm(big_dict,count_dict):
			print(b[start:end+1])
		if big_dict.get(b[start])!=None:
			big_dict[b[start]]-=1
		start+=1
		end+=1
		if end==len(b):
			break
		if big_dict.get(b[end])!=None:
			big_dict[b[end]]+=1
		# print(big_dict)


get_all_perms("abbc","cbabadcbbabbcbabaabccbabc")