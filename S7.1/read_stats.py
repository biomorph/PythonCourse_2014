__author__ = 'ravi'
import numpy as np

def parse_reads(fastq_file):
    fastq_fh = open(fastq_file,'r')
    nuc_array = []
    quality_array = []
    short_lengths = 0
    while True:
        id = fastq_fh.readline().strip()
        if id == '': break
        seq = fastq_fh.readline().strip()
        id2 = fastq_fh.readline().strip()
        qual_line = fastq_fh.readline().strip()
        if len(seq) != 50 or len(qual_line) != 50: continue
        qual_values = [ord(qual) -33 for qual in qual_line]
        nuc_array.append(list(seq))
        quality_array.append(qual_values)

    return quality_array, nuc_array


def get_per_position_quality(quality_array):

    np_qual_array = np.array(quality_array)
    return np.mean(np_qual_array, axis=0)

def get_per_position_base_comp(nuc_array):
    np_nuc_array = np.array(nuc_array)
    avg_a = []
    avg_t = []
    avg_g = []
    avg_c = []
    avg_n = []
    #print np_nuc_array
    read_num = float(len(np_nuc_array))
    for i in range(len(np_nuc_array[0])):
        a_freq = 100*np.sum(np_nuc_array[:,i] == 'A')/read_num
        t_freq = 100*np.sum(np_nuc_array[:,i] == 'T')/read_num
        g_freq = 100*np.sum(np_nuc_array[:,i] == 'G')/read_num
        c_freq = 100*np.sum(np_nuc_array[:,i] == 'C')/read_num
        n_freq = 100*np.sum(np_nuc_array[:,i] == 'N')/read_num
        avg_a.append(a_freq)
        avg_t.append(t_freq)
        avg_g.append(g_freq)
        avg_c.append(c_freq)
        avg_n.append(n_freq)
    return np.array([avg_a,avg_t,avg_c,avg_g,avg_n])



quality_array, nuc_array = parse_reads('E_coli_reads.fastq')

avg_quality_per_position = get_per_position_quality(quality_array)

base_freq_per_position = get_per_position_base_comp(nuc_array)


print avg_quality_per_position, base_freq_per_position
#print quality_array, nuc_array
