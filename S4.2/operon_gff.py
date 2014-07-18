__author__ = 'ravi'

operon_fh = open('gnc511145.named','r') # open operon significance file

operon_pair_significance_list = [] # this is a list of gene pairs and significance
operon_fh.next() # skips the header line

# parse operon significance file
for line in operon_fh:
    line = line.strip().split("\t")[4:7]
    if '' not in line: operon_pair_significance_list.append(line) #there are some entries that are missing columns ftsB entries
operon_fh.close()

genes_or_operon_list = [] # this is a list with either singleton genes or pairs of significant operons

# genes with significant interaction are paired as possible operons and those pairs that are not are split into singletons
for gene_pairs in operon_pair_significance_list:
    if gene_pairs[2] == 'FALSE':
        genes_or_operon_list.append([gene_pairs[0]])
        genes_or_operon_list.append([gene_pairs[1]])
    else:
        genes_or_operon_list.append(gene_pairs[0:2])


final_operon_list = [] # this is the list of lists with singletons or merged operons

intermediate_operon = [] # this is the intermediate list with merged operons

# go through the list of singletons and operon pairs to combine ones where the last element of a multiple operon list and the first element of the next match

# in short this part condenses overlapping gene pairs and singletons
while len(genes_or_operon_list) > 1:
    if genes_or_operon_list.pop()[0] == genes_or_operon_list[-1][-1]:
        intermediate_operon = genes_or_operon_list[-1][:-1] + intermediate_operon
    else:
        final_operon_list.append(intermediate_operon)
        intermediate_operon = genes_or_operon_list[-1]
final_operon_list.append(genes_or_operon_list[0])
final_operon_list.reverse()
print final_operon_list

gene_list_fh = open('full_genelist','r') # open full gene list file

gene_list_dict = {} # dict with genes as keys and list of coordinates and strand as values

gene_list_fh.next() # skip header

# parse the gene list file and store in a dict
for line in gene_list_fh:
    line = line.strip().split("\t")[4:9]
    gene_list_dict[line[-1]] = line[:-2]


# for each gene singleton or operon construct a gff line with coordinates and strand
for feature in final_operon_list:
    # making sure to only print out non empty features
    if feature: print "Chromosome\tMicrobesOnline\toperon\t"+ gene_list_dict[feature[0]][0] + "\t" + \
                      gene_list_dict[feature[-1]][1] + "\t.\t" + gene_list_dict[feature[0]][2] + "\t.\toperonName \"" \
                      + "-".join(feature) + "\";"