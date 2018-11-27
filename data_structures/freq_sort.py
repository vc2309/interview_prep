def invert_map(map):
	inverted = {val:[] for val in map.values()}
	for key in map.keys():
		inverted[map[key]].append(key)
	return inverted


def freq_sort(string):
	word_2_freq = {i:0 for i in string}
	for i in string:
		word_2_freq[i]+=1

	freq_2_word = invert_map(word_2_freq)
	#sort lexicographically
	for key in freq_2_word.keys():
		freq_2_word[key]=sorted(freq_2_word[key])

	newstr = ""
	for freq in sorted(freq_2_word.keys(),reverse=True):
		newstr+="".join(freq_2_word[freq])

	return newstr