__author__ = 'ravi'

'''
# 1 a)
list_of_letters = ['a', 'a', 'b', 'c','c','c','d','e']
print 'ORIGINAL'
set_of_letters = set(list_of_letters)
print set_of_letters

print 'DISCARD'
set_of_letters.discard('q')
print set_of_letters

print 'REMOVE'
set_of_letters.remove('q')
print set_of_letters

# remove throws an error if it doesn't find the element being removed, discard removes it if found and if it doesn't no error


# b) beer list

beer_list = set(['IPA','Lager','Stout','Belgian','Amber'])

while len(beer_list) > 0:
    choice = raw_input("What would you like to drink? ")
    try:
        beer_list.remove(choice)
        print "Here is your ", choice

    except KeyError:
        print "Sorry we're out of ", choice

print "We're out of beer"

# 2 a) Modify the fasta parser to handle exceptions

def parse_fasta(fasta_file):
    fasta_dict = {}
    try:
        fasta_fh = open(fasta_file,'r')
        base_set = set(['A','T','G','C','N','a','t','g','c','n'])
        gene_name = ''
        for line in fasta_fh:
            line = line.strip()
            if line[0] == '>':
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
    except IOError:
        print "Couldn't find the file",fasta_file



print parse_fasta('testFasta.fa')

# 3) For parsing zipped fastas
import mimetypes
import gzip
import os
import sys

def open_file_by_mimetype(file_name):
    if os.path.exists(file_name):
        if mimetypes.guess_type(file_name)[1] == 'gzip':
            return gzip.open(file_name,'r')
        else:
            return open(file_name,'r')
    else:
        sys.exit("File does not exist")


def read_fasta(fasta_file):
    fasta_dict = {}
    fasta_fh = open_file_by_mimetype(fasta_file)
    base_set = set(['A','T','G','C','N','a','t','g','c','n'])
    gene_name = ''
    for line in fasta_fh:
        line = line.strip()
        if line[0] == '>':
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


import sequence_tools

print sequence_tools.read_fasta('testFasta.fa')

print "Git difference"
'''
from Bio import  SeqIO

fasta_fh = open('testFasta.fa','r')
fasta = SeqIO.parse(fasta_fh,'fasta')
for entry in fasta:
    print entry.seq
