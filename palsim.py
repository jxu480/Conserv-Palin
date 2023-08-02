import random
import itertools
import re

def randseq(length):
	seq = ''
	for i in range(length):
		seq += random.choice('ACGT')
	return seq

def rc(seq):
	anti = ''
	for nt in seq:
		if   nt == 'A': anti = 'T' + anti
		elif nt == 'C': anti = 'G' + anti
		elif nt == 'G': anti = 'C' + anti
		elif nt == 'T': anti = 'A' + anti
		else: raise Exception('unexpected')
	return anti

def palindromes(length):
	half = length//2
	pals = []
	for t in itertools.product('ACGT', repeat=half):
		if length % 2 == 0:
			pal = ''.join(t) + rc(''.join(t))
		else:
			pal = ''.join(t) + '.' + rc(''.join(t))
		pals.append(pal)
	return pals

seq = randseq(100000)

score = {
	6: 1,
	7: 1,
	8: 4,
	9: 4,
	10: 16
}

win = 1000

for i in range(0, len(seq) - win+1, 1):
	pscore = 0
	for palen in range(6, 11):
		for pal in palindromes(palen):
			m = re.findall(pal, seq[i:i+win])
			s = len(m) * score[palen]
			pscore += s
	print(i, pscore)