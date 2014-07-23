__author__ = 'ravi'
from file_tools import open_file_by_mimetype

def parse_fasta(fasta_file):
    fasta_dict = {}
    fasta_fh = open(fasta_file,'r')
    for line in fasta_fh:
        line = line.strip()
        if line[0] == '>':
            gene_name = line[1:]
            fasta_dict[gene_name] = ''
        else:
            fasta_dict[gene_name] += line
    print "Fasta_Parser"
    return fasta_dict

def reverse_complement(DNA):
    reverse_complement = ''
    dna_dict = {'A':'T','T':'A','G':'C','C':'G','N':'N'}
    bases = set(DNA.upper())
    if not set(['A','T','G','C','N']).issuperset(bases):
        print "Does your sequence have invalid bases?"

    else:
        reverse = DNA.upper()[::-1]
        for base in reverse:
            reverse_complement += dna_dict[base]
    return reverse_complement

def read_fasta(fasta_file):
    fasta_dict = {}
    fasta_fh = open_file_by_mimetype(fasta_file)
    base_set = set(['A','T','G','C','N','a','t','g','c','n'])
    gene_name = ''
    for line in fasta_fh:
        line = line.strip()
        if line.startswith('>'):
            gene_name = line[1:]
            fasta_dict[gene_name] = []
        else:
            if set(line).issubset(base_set):
                fasta_dict[gene_name].append(line)
            else:
                print 'Your Fasta sequence has invalid base/s',','.join(set(line).difference(base_set)),' in ', gene_name
                fasta_dict = {}
                break
    for entry in fasta_dict:
        fasta_dict[entry] = ''.join(fasta_dict[entry])
        if not fasta_dict[entry].islower() and not fasta_dict[entry].isupper():
            print "Your fasta sequences have a mix of upper and lower case bases"
    return fasta_dict
