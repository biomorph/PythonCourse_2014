__author__ = 'ravi'
'''
# 1. A dictionary of dictionaries
org_gene_dict = {}

org_gene_dict['Human genes']= {'TallnessGene': 'AATAGCAG', 'SmartnessGene': 'TGACGGA'}


org_gene_dict['Mouse genes'] = {'FuzzynessGene': 'CCCCCCA', 'BeadyLittleEyesGene': 'ATAGCGC'}

org_gene_dict['Rat genes'] = {'FuzzynessGene': 'CCCTCCA', 'BiggerThanMouseGene': 'GGACAATT'}

print org_gene_dict
print org_gene_dict['Human genes'].keys()
print org_gene_dict['Mouse genes']['FuzzynessGene']
print org_gene_dict['Rat genes']['FuzzynessGene']
print org_gene_dict['Human genes']['TallnessGene'][2]


# 2. A list of lists
# a)
experiment_data = []

for i in range(3): experiment_data.append([])

for i in [2,3,5,5]: experiment_data[0].append(i)
for i in [2,2,4,5]: experiment_data[1].append(i)
for i in [3,3,4,6]: experiment_data[2].append(i)

print experiment_data

# b)
experiment_data = [[],[],[]]

for i in [2,3,5,5]: experiment_data[0].append(i)
for i in [2,2,4,5]: experiment_data[1].append(i)
for i in [3,3,4,6]: experiment_data[2].append(i)

print experiment_data

# c)
experiment_data = [[2, 3, 5, 5], [2, 2, 4, 5], [3, 3, 4, 6]]

print experiment_data

# 3. A dictionary of lists

# a)
bfactor_dict = {}
bfactor_dict['Human'] = []
bfactor_dict['Mouse'] = []
bfactor_dict['Rat'] = []

for i in [5,4,6,7]: bfactor_dict['Human'].append(i)
for i in [8,12,11,14]: bfactor_dict['Mouse'].append(i)
for i in [10,11,13,15]: bfactor_dict['Rat'].append(i)

print bfactor_dict

# b)
bfactor_dict = {'Rat': [10, 11, 13, 15], 'Mouse': [8, 12, 11, 14], 'Human': [5, 4, 6, 7]}

print bfactor_dict


# 4. Run lola run

run1 = [2,3,5,5]
run2 = [2,2,4,5]
run3 = [3,3,4,6]

listOfRuns = [run1,run2,run3]

print listOfRuns

# a)
run1[0] = 200

print listOfRuns

listOfRuns = [run1[:], run2[:], run3[:]]

print listOfRuns

run1[0] = 20000000

print listOfRuns
'''
# 5. Multiplying Lists

lili = 3*[[0]]
lili[0].append('i belong first')

print lili
