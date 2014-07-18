__author__ = 'ravi'
#initialize list to store sequence
protSeq = []
#open pdb file
f1 = open('2Q6H.pdb', 'r')
#loop over lines in file
for next in f1:
    #identify lines that contain sequences
    if next[:6] == 'SEQRES':
        #strip away white space and
        #convert line into list
        line = next.strip().split()
        #delete descriptor information
        #at beginning of each line
        del line[:4]
        #loop over amino acids in line
        for aa in line:
            #add to sequence list
            protSeq.append(aa)
#close file
f1.close()

print len(protSeq)

aa_dict = {}

for aa in protSeq:
    if aa in aa_dict: aa_dict[aa] += 1
    else: aa_dict[aa] = 1

total = 0
for aa in sorted(aa_dict.keys()):
    print aa, ":", aa_dict[aa]
    total += aa_dict[aa]

print total, len(aa_dict)

aa_set = set(protSeq)
#print aa_set, len(aa_set)

for aa in sorted(aa_set):
    print aa, ":", protSeq.count(aa)
