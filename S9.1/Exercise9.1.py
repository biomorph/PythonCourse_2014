__author__ = 'ravi'
# generate random reads fastq

import numpy as np
import sys
from sequence_tools import read_fasta
'''
N = int(sys.argv[1])

genome_sequence = read_fasta('random_genome.fa')['Random_genome']

five_prime_ends = np.random.randint(0,len(genome_sequence),size=N)

fastq_filename = str(N)+'simulated.fastq'
fastq_fh = open(fastq_filename,'w')

for i,start in enumerate(five_prime_ends):
    read_sequence = genome_sequence[start:start+100]
    read_quality = 'P'*len(read_sequence)
    fastq_fh.write('\n'.join(['@Read'+str(i+1),read_sequence,'+',read_quality,'']))

fastq_fh.close()

# get expected coverage (C=N*L/G) vs observed coverage
import pandas
genome_sequence = read_fasta('random_genome.fa')['Random_genome']
genome_length = len(genome_sequence)
coverage_file = sys.argv[1]
coverage = pandas.read_table(coverage_file,header=None)

max_coverage = max(coverage.icol(3))

total_reads = 0
sum = 0
for i in range(1,max_coverage+1):
    number_of_reads = len(coverage[coverage.icol(3)==i])
    total_reads += number_of_reads
    sum += i*number_of_reads
    print "number of sites with %sX coverage %s" %(i,number_of_reads)

print "average_coverage =", sum/total_reads
print "expected_coverage=", 100*int(coverage_file.split('s')[0])/genome_length
print genome_length
'''
# 2 LRT for diff expression
import numpy as np
import math

diff_array = np.loadtxt('diff.txt')
nondiff_array = np.loadtxt('nodiff.txt')

def get_LR(N):
    avg = (N[0]+N[1])/2
    return 2*(N[0]*math.log(N[0])+ N[1]*math.log(N[1])- 2*avg*math.log(avg))



LRT_array_diff = np.apply_along_axis(get_LR,1,diff_array)
LRT_array_nodiff = np.apply_along_axis(get_LR,1,nondiff_array)
print len(LRT_array_diff[LRT_array_diff>3.84])
print len(LRT_array_nodiff[LRT_array_nodiff>3.84])


nodiff_nbinom_array = np.loadtxt('nodif.nbinom.txt')
LRT_array_nodiff_nbinom = np.apply_along_axis(get_LR,1,nodiff_nbinom_array)
print len(LRT_array_nodiff_nbinom[LRT_array_nodiff_nbinom>3.84])

#print get_LR([50,30])
#print diff_array
#print nondiff_array



