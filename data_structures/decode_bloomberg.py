def decode(string):
	if not string:
		return
	curr_char= string[0]
	curr_l=1
	new_str=""
	for i in string[1:]:
		if i!=curr_char:
			new_str+=("{}{}".format(curr_char,str(curr_l)))
			curr_char=i
			curr_l=1
		else:
			curr_l+=1
	return new_str

def main():
	string = input("enter input")
	print(decode(string))

if __name__ == '__main__':
	main()