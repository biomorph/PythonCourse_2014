__author__ = 'ravi'
import marshal
import sys
import os
from sequence_tools import read_fasta, reverse_complement
def make_kmer_dict(sequence,k):
    kmer_dict = {}
    for i in range(len(sequence)-k):
        kmer = sequence[i:i+k]
        if kmer in kmer_dict:
            kmer_dict[kmer].append(i+1)
        else: kmer_dict[kmer] = [i+1]

    return kmer_dict

def parse_fastq(fastq_file):
    fastq_fh = open(fastq_file,'r')
    read_list = []
    while True:
        id = fastq_fh.readline().strip()
        if id == '': break
        seq = fastq_fh.readline().strip()
        fastq_fh.readline()
        fastq_fh.readline()
        read_list.append(seq)
    return read_list

def search_dict(read, forward_dict, reverse_dict, k):
    hits = []
    match = False
    strand = '+'
    if read[0:k] in forward_dict:
        hits.append([read, forward_dict[read[0:k]], strand])
        match = True
    if read[0:k] in reverse_dict:
        strand = '-'
        hits.append([read, reverse_dict[read[0:k]], strand])
        match = True
    if not match: hits = ['Unmapped']
    return hits

fasta_dict = read_fasta('E_coli_genome.fa')
forward_genome = fasta_dict[fasta_dict.keys()[0]]
reverse_genome = reverse_complement(forward_genome)

k = 11

forward_dict = {}
reverse_dict = {}
if os.path.exists('forward.dict'):
    forward_dict = marshal.load(open('forward.dict','r'))
else:
    forward_dict = make_kmer_dict(forward_genome,k)
    marshal.dump(forward_dict, open('forward.dict','w'))

if os.path.exists('reverse.dict'):
    reverse_dict = marshal.load(open('reverse.dict','r'))
else:
    reverse_dict = make_kmer_dict(reverse_genome,k)
    marshal.dump(reverse_dict, open('reverse.dict','w'))


read_list = parse_fastq('test.fastq')

for read in read_list:
    print search_dict(read,forward_dict,reverse_dict, k)


