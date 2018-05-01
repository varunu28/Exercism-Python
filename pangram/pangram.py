def is_pangram(sentence):
	word_list = []
	for s in sentence.lower():
		if s.isalpha() and s not in word_list:
			word_list.append(s)
	return len(word_list) == 26
