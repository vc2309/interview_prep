def power_set(elems):
	set_queue = ([elems]).extend([e for e in elems])
	sets = {i:True for i in set_queue}

	for i in range(len(elems)-1):
		window = elems[i:i+1]
		rem = (elems[:i]).extend(elems[i+1:])
		for elem in rem:
			for i in set_queue:
				sub = i.append(rem)
				if not sets.get(sub):
					set_queue.append(sub)
					sets[sub]=True
		if not sets.get(window):
			set_queue.append(window)
			sets[window]=True
	print( set_queue)

def main():
	main_set = ["a","b","c"]
	power_set(main_set)

if __name__ == '__main__':
	main()
