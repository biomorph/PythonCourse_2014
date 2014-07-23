__author__ = 'ravi'
from sequence_tools import read_fasta, reverse_complement

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

def search_read(read, forward_genome, reverse_genome):
    hits = []
    strand = '+'
    match = False
    for j,genome in enumerate([forward_genome,reverse_genome]):
        for i in range(len(genome)-len(read)+1):
            if genome[i:i+len(read)] == read:
                if j == 1: strand = '-'
                hits.append([read,i+1,i+len(read)+1,strand])
                match = True
    if not match: hits = ['Unmapped']
    return hits

fasta_dict = read_fasta('E_coli_genome.fa')
forward_genome = fasta_dict[fasta_dict.keys()[0]]
reverse_genome = reverse_complement(forward_genome)
fastq_list = parse_fastq('test.fastq')

for read in fastq_list:
    print search_read(read,forward_genome,reverse_genome)




