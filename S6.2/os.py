__author__ = 'ravi'
import subprocess as sp
'''
proc = sp.Popen(['ls', '-l'], stdout=sp.PIPE)
# The sp.PIPE is a mechanism that allows the output to be redirected to
# wherever you point it. In this case, to our subprocess object named proc.
# The next step is to get the data out of the object and into a data structure
# that we can organize however we see fit.

# we use the method below to get a tuple of two things: the stdout and the stderr
proc_output = proc.communicate()
print "------------------------"
print "We got a tuple\nWith the first part being:\n", proc_output[0], \
"\nand the second being:\n", proc_output[1]
print "------------------------"

# Once we use the .communicate() method, the stdout and stderr are gone from the proc object.
print "------------------------"
print "and if we don't format anything, we see the tuple like this:\n", proc_output
print "------------------------"

# But we could easily convert this into a friendlier structure
stdoutlist = proc_output[0].split('\n')
print "------------------------"
print "And now we see the first half of the tuple as a list of lines" \
+ "of output from our subprocess:\n", stdoutlist
print "------------------------"
'''

program = 'blastn'
queryseq = 'query.fasta'
database = 'yeast.nt'

proc = sp.Popen([program, '-query', queryseq, '-db', database], stdout=sp.PIPE)

output = proc.communicate()
outlist = output[0].split('\n')
for line in outlist: print line

import subprocess as sp

# some arguments for running BLAST
program = 'blastn'
queryseq = 'query.fasta'
database = 'yeast.nt'

# open a filehandle for our output file, we'll use the append flag in case
# we want to collect multiple queries worth of output

try:
    outfh = open('blastn_output', 'a')
except:
    print "Error opening output file: blastn_output"

proc = sp.Popen([program, '-query', queryseq, '-db', database], stdout=outfh)
