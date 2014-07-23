__author__ = 'ravi'
# 1 blastn format output
import subprocess as sp
'''
gid_dict = {'NC_001224.1': 'mitochondrion',
'NC_001133.1': 'chromosome I',
'NC_001134.1': 'chromosome II',
'NC_001135.1': 'chromosome III',
'NC_001136.2': 'chromosome IV',
'NC_001137.2': 'chromosome V',
'NC_001138.1': 'chromosome VI',
'NC_001139.1': 'chromosome VII',
'NC_001140.2': 'chromosome VIII',
'NC_001141.1': 'chromosome IX',
'NC_001142.1': 'chromosome X',
'NC_001143.1': 'chromosome XI',
'NC_001144.1': 'chromosome XII',
'NC_001145.1': 'chromosome XIII',
'NC_001146.1': 'chromosome XIV',
'NC_001147.1': 'chromosome XV',
'NC_001148.1': 'chromosome XVI'}

program = 'blastn'
queryseq = 'pombe.fa'
database = 'yeast.nt'
evalue = '1e-02'
output_format = '6 sacc length evalue pident'
proc = sp.Popen([program, '-query', queryseq, '-db', database, '-evalue', evalue, '-outfmt',output_format ], stdout=sp.PIPE)

output = proc.communicate()

blast_out_dict = {}
for line in output[0].strip().split("\n"):
    line = line.split("\t")
    chromosome = gid_dict[line[0].rsplit("|")[-2]]
    if chromosome not in blast_out_dict:
        blast_out_dict[chromosome] = [line[1:]]
    else:
        blast_out_dict[chromosome] += [line[1:]]
print blast_out_dict


# 2 blastp
from sequence_tools import read_fasta

aa_code_fh = open('aa_code','r')
codon_dict = {}

for line in aa_code_fh:
    line = line.strip().split()
    aa_code = line[0].split('/')[1]
    codons = line[1:]
    codons = [codon.replace(',', '')for codon in codons]
    codons = [codon.replace('U', 'T')for codon in codons]
    for codon in codons: codon_dict[codon] = aa_code

aa_code_fh.close()

fasta_dict = read_fasta('query.fasta')
translated_query_fh = open('query_trans.fasta','w')

for sequence in fasta_dict:
    nucleotides = fasta_dict[sequence]
    protein_seq = []
    for i in range(0,len(nucleotides),3):
        codon = nucleotides[i:i+3]
        if codon in codon_dict and codon_dict[codon] is not '*': protein_seq.append(codon_dict[codon])
        else: break
    translated_query_fh.write('>%s\n'%(sequence))
    translated_query_fh.write(''.join(protein_seq))
'''

program = '/Users/ravi/PythonCourse/ProgramFiles/ncbi-blast-2.2.26+/bin/blastp'
queryseq = 'query_trans.fasta'
database = 'yeast.aa'
evalue = '1e-08'
output_format = '6 sacc length evalue pident'
proc = sp.Popen([program, '-query', queryseq, '-db', database, '-evalue', evalue, '-outfmt',output_format ], stdout=sp.PIPE)

output = proc.communicate()

print output[0]







