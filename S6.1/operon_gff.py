__author__ = 'ravi'
import pandas
operon_fh = open('gnc511145.named','r') # open operon significance file

operon_df = pandas.read_table('gnc511145.named')


genes_or_operon_list = []


for row_num in operon_df.index:
    row_data = operon_df.ix[row_num]
   # print row_data['Name1']
    if row_data['bOp'] and type(row_data['Name1']) is str: genes_or_operon_list.append(list(row_data['Name1':'Name2']))
    elif not row_data['bOp'] and type(row_data['Name1']) is str:
        genes_or_operon_list.append([row_data['Name1']])
        genes_or_operon_list.append([row_data['Name2']])
print genes_or_operon_list



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
#print final_operon_list



gene_list_df = pandas.read_table('full_genelist')

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
    if len(feature)>1:
        start = str(gene_list_df[gene_list_df.name==feature[0]].start)
        #print start

        #print "Chromosome\tMicrobesOnline\toperon\t"+ gene_list_df[gene_list_df.name==feature[0]][0] + "\t" + \
                      #gene_list_dict[feature[-1]][1] + "\t.\t" + gene_list_dict[feature[0]][2] + "\t.\toperonName \"" \
                      #+ "-".join(feature) + "\";"
    if len(feature)==1:
        if gene_list_dict[feature[0]][2] == '-':
            print "Chromosome\tMicrobesOnline\toperon\t"+ gene_list_dict[feature[0]][1] + "\t" + \
                      gene_list_dict[feature[-1]][0] + "\t.\t" + gene_list_dict[feature[0]][2] + "\t.\toperonName \"" \
                      + "-".join(feature) + "\";"
        else:
            print "Chromosome\tMicrobesOnline\toperon\t"+ gene_list_dict[feature[0]][0] + "\t" + \
                      gene_list_dict[feature[-1]][1] + "\t.\t" + gene_list_dict[feature[0]][2] + "\t.\toperonName \"" \
                      + "-".join(feature) + "\";"