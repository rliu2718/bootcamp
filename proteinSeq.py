def proteinSeq(filename, aa_start=0, aa_end=None):
	"""Takes protein sequence file, returns protein fragment aa_start to aa_end"""

	protein_seq = open(filename, 'r').read().replace('\n', '')
			
	if aa_end==None:
		aa_end = aa_start
	
	print('Length:', len(protein_seq))
	print(protein_seq, '\n')
	print('Amino acids', str(aa_start), 'to', str(aa_end)+':')
	
	return str(protein_seq[aa_start-1: aa_end])