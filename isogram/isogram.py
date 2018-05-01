def is_isogram(string):
	flag = False
	string_rep = ""
	for s in string:
		if s.isalpha() and s in string_rep.lower():
			return False
		
		if s.isalpha():
			string_rep = string_rep + s
	return True
