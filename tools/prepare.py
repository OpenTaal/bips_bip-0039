#!/usr/bin/env python3

from os.path import isdir

allowed = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w')
forbidden = 'ij' 

def check(word):
	for char in word:
		if char not in allowed:
			return False
	if forbidden in word:
		return False
	return True


if not isdir('../downloads/bips-master'):
	print('ERROR: First run ./download.sh')
	exit(1)

out = open('../downloads/word-frequency.tsv', 'w')
total_in = 0
total_out = 0
for line in open('../downloads/correct-words-with-frequency.tsv'):
	total_in += 1
	freq, word = line[:-1].split('\t')
	if check(word):
		out.write('{}\t{}\n'.format(freq, word))
		total_out += 1
print('{} {}'.format(total_in, total_out))
