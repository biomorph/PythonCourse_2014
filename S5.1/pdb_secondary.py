import sys, os

full_seq = []
helix_aa = []
sheet_aa = []

import sys, os

full_seq = []
helix_aa = []
sheet_aa = []
atoms = []
f1 = open('1N1F.pdb' ,'r')
for next in f1:
    tmp = next.strip().split()
    if tmp[0] == 'SEQRES':
        if tmp[2] == 'A':
            full_seq.extend(tmp[4:])
    elif tmp[0] == 'HELIX':
        try:
            int(tmp[5])
        except:
            tmp[5] = tmp[5][:-1]
        helix_aa.append(tmp[:9])
    elif tmp[0] == 'SHEET':
        sheet_aa.append(tmp[:10])
    elif tmp[0] == 'ATOM':
        if len(tmp) < 12:
            begin = tmp[0:2]
            end = tmp[3:]
            middle = [tmp[2][:3], tmp[2][4:]]
            tmp = begin + middle + end
        try:
            int(tmp[5])
        except:
            continue
        atoms.append(tmp)

######################

num_helix_res = 0.0
print "There are %s residues in the sequence" % len(full_seq)

# Set up a listing of features by residue, then fill it in as we go along
feature = ['Other']*(10000)

for aa in helix_aa:
    # We add 1 because there are b-a+1 residues between a and b, inclusive
    num_helix_res += float(aa[8]) - float(aa[5]) + 1
    for i in range(int(aa[5]), int(aa[8])+1):
        feature[i] = 'Helix'

num_sheet_res = 0.0
for sheet in sheet_aa:
    num_sheet_res += float(sheet[9]) - float(sheet[6]) + 1
    for i in range(int(sheet[6]), int(sheet[9])+1):
        feature[i] = 'Sheet'


 # atom[4] == chain id
 # atom[5] == residue #
 # atom[10] == b-factor


helix_bfactors = {}
sheet_bfactors = {}
other_bfactors = {}

for atom in atoms:
    Chain = atom[4]
    BFactor = float(atom[10])
    ResidueNum = int(atom[5])

    if feature[ResidueNum] == 'Helix':
        if Chain not in helix_bfactors:
            helix_bfactors[Chain] = []
        helix_bfactors[Chain].append(BFactor)
    elif feature[ResidueNum] == 'Sheet':
        if Chain not in sheet_bfactors:
            sheet_bfactors[Chain] = []
        sheet_bfactors[Chain].append(BFactor)
    else:
        if Chain not in sheet_bfactors:
            other_bfactors[Chain] = []
        other_bfactors[Chain].append(BFactor)

for chain in helix_bfactors:
    # I could have used any of the different bfactor listings
    avg_helix, avg_sheet, avg_other = 0,0,0
    if chain in helix_bfactors: avg_helix = sum(helix_bfactors[chain])/len(helix_bfactors[chain])
    if chain in sheet_bfactors: avg_sheet = sum(sheet_bfactors[chain])/len(sheet_bfactors[chain])
    if chain in other_bfactors: avg_other = sum(other_bfactors[chain])/len(other_bfactors[chain])
    print '%s\t %5f\t %5f\t %5f' % (chain, avg_helix, avg_sheet, avg_other)