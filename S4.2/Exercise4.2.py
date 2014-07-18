__author__ = 'ravi'
'''
# 3c) BioPython sequence fasta manipulation
from Bio import SeqIO
chromosomes = [rec for rec in SeqIO.parse('yeast_genome.fa', 'fasta')]

rev_chromosomes = []
for chr in chromosomes:
    chr.seq = chr.seq.reverse_complement()
    chr.id = chr.name + "_RevC"
    rev_chromosomes.append(chr)
revC_fh = open('yeast_genome_revC.fa','w')
SeqIO.write(rev_chromosomes,revC_fh,'fasta')
'''
#3d) one aa code to 3 aa code

threecode = {'A':'Ala', 'B':'Asx', 'C':'Cys', 'D':'Asp',
                 'E':'Glu', 'F':'Phe', 'G':'Gly', 'H':'His',
                 'I':'Ile', 'K':'Lys', 'L':'Leu', 'M':'Met',
                 'N':'Asn', 'P':'Pro', 'Q':'Gln', 'R':'Arg',
                 'S':'Ser', 'T':'Thr', 'V':'Val', 'W':'Trp',
                 'Y':'Tyr', 'Z':'Glx', 'X':'Xaa', '*':'Ter',
                 'U':'Sel', 'O':'Pyl', 'J':'Xle',
                 }
protein_string = "MADHNTTAFW"
three_letter_protein_string = []

for aa in protein_string:
    three_letter_protein_string.append(threecode[aa])

print ''.join(three_letter_protein_string)