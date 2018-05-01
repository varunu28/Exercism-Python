def to_rna(dna_strand):
	rna_strand = ""
	for d in dna_strand:
		new_d = d
		if d == "C":
			new_d = "G"
		elif d == "G":
			new_d = "C"
		elif d == "T":
			new_d = "A"
		else:
			new_d = "U"
		rna_strand = rna_strand + new_d
	return rna_strand
