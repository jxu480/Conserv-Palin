# find all the palindromes in the given sequences
# importing seq
# exporting palindrome density
'''
Ways of speeding it up:
Write it in a different program (ex, JAVA, Julia)
Change the program
	For every base check if it's in a palindrome of 6, 7, 8, 9, 10 length
		Only going over the genome once
	Then, bring a window and collect all the information in that corresponding window
	
Run it over different CPUS
Ex; 16
	Cut the genome up in to 16 pieces, run the functions over each of the 16 strands in 
	the different CPUS, merge the data together at the end
'''

import sys
import itertools
import mcb185
import re

# Create list of palindromes of specified length
def pcreate(plen):
	plist = list(''.join(tups) for tups in itertools.product('ACGT', repeat= int(plen/2)))
	palin = []
	if plen % 2 == 0:
		for p in plist:
			palin.append(p + mcb185.reverse(p))
	else:
		for p in plist:
			palin.append(p + '.' + mcb185.reverse(p))
	return palin

# Checks the list for variation, removes the common ones (AAATTT, etc)
def variation(palin):
	psorted = []
	for p in palin:
		v = 0
		nt = {'A':p.count('A'), 'C':p.count('C'), 'G':p.count('G'), 'T':p.count('T')}
		for k in nt:
			if nt[k] != 0:
				v += 1
		if v > 2:
			psorted.append(p)
	return psorted

winsiz = 200
palin_score = {6:1, 7:1, 8:4, 9:4, 10:16, 11:16}

# Reads each sequence in the window, finds all matches of all palindromes
for name, seq in mcb185.read_fasta(sys.argv[1]):
	for i in range(len(seq) - winsiz + 1):
		pscore = 0
		for j in range(6, 11):
			ppalin = variation(pcreate(j))
			for p in ppalin:
				match = re.findall(p, seq[i:i+winsiz])
				pscore += palin_score[j] * len(match)
				
		print(i, pscore)

		
'''		

python3 palindromesearch.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz 
python3 palindromesearch.py fake.fasta 
'''