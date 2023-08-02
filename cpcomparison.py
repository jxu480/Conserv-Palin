import sys
from statistics import mean, stdev
# zscore

def filestats(filename):
	vals = []
	with open(filename) as fp:
		for line in fp:
			f = line.split()
			vals.append(int(f[2]))
	return mean(vals), stdev(vals)

cm, cs = filestats(sys.argv[1])
pm, ps = filestats(sys.argv[2])

cons = {}
with open(sys.argv[1]) as fp:
	for line in fp:
		f = line.split()
		cons[int(f[1])] = int(f[2])

exons = {}
with open(sys.argv[3]) as fp:
	for line in fp:
		f = line.split()
		beg = int(f[3])
		end = int(f[4])
		for i in range(beg - 100, end + 101):
			exons[i] = True

with open(sys.argv[2]) as fp:
	for line in fp:
		chrom, coord, palin = line.split()
		coord = int(coord)
		if coord in exons:
			continue
		palin = int(palin)
		if coord in cons:
			zc = (cons[coord] - cm)/cs
			zp = (palin - pm)/ps
			print(coord, cons[coord], palin, f'{zc:.1f}', f'{zp:.1f}', f'{zc + zp:.1f}')

