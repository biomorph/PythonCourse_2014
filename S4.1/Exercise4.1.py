__author__ = 'ravi'
'''
# 1. Practice with functions
def double_num(x):
    print x*2
    return x*2

def multiply(x,y):
    print x*y
    return x*y

def product_list(xs):
    print xs[0]*xs[1]
    return xs[0]*xs[1]

double_num(4)
multiply(3,4)
product_list([1,5,6])


#2. What happens in functions doesn't always stay in there

def increment(x):
    x = x + 1

y = 1
print y
increment(y)
print y

def change_list(X):
    X[0] = 'x'

y = [1,2,4]
print y
change_list(y)
print y

def change_dict(Z):
    Z.update({'x':'y'})

y = {'a':'b', 'd':'e', 'l':'m'}
print y
change_dict(y)
print y


# 3. reverse complement

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
    print reverse_complement

reverse_complement('ATGGAAATTTGGCCAATTNNNRRR')
'''
from sequence_tools import  parse_fasta

print parse_fasta('testFasta.fa')['gene3']
