__author__ = 'ravi'
import numpy as np
'''
# 1a) divide an array by 1.5
def divide_by(nparray):
    return nparray/1.5

float_array = np.arange(10,dtype=float)

print float_array
print divide_by(float_array)


# 1b) get outliers
def outliers(random_array, mean, stdev):
    return random_array[[random_array>mean+stdev]]

mean, stdev = 3.2, 1.1
random_float_array = np.random.normal(mean,stdev,100)
print random_float_array
print outliers(random_float_array, mean, stdev)

# 1c) y = e^x
def exponential_residual(x_array):
    y_array = np.exp(x_array)
    random_exp_array = np.random.exponential(1,11)
    return np.sum(random_exp_array-y_array)
    #print np.sort(random_exp_array)
    #print y_array

x_array = np.arange(11)
print exponential_residual(x_array)


#2a) pyrimidine substring distance
import re
from Bio import SeqIO
def find_substring_location(substring, sequence):
   match_list = [match.start() for match in re.finditer(substring,sequence)]
   diff_list = [match_list[i+1]-match_list[i] for i in range(len(match_list)-1)]
   return diff_list

    #return match_indices

sequence = 'ATGAGACGTAGTGCCAGTAGCGCGATGTAGCGATGACGCATGACGCGCGACGCGCGAGTGAGCCATACGCACGCATTGGCA'
substring = '[CT]'

#print find_substring_location(substring,sequence)

fasta_fh = open('testFasta.fa','r')
fasta_records = SeqIO.parse(fasta_fh,'fasta')
distance_array = []
for record in fasta_records:
    distance_array+=find_substring_location(substring,str(record.seq))


print distance_array
print np.histogram(distance_array)
'''


