__author__ = 'ravi'
# 1 Scatter plots for pair-wise RPKM comparisons
import matplotlib.pyplot as plt
import pandas
'''
condition_pairs = [('control_20min_0','control_60min_0','blue'),('control_20min_0','20bicyclomycin_20min_0','green'),
                   ('control_20min_0','100bicyclomycin_20min_0','red'),('20bicyclomycin_20min_0','100bicyclomycin_20min_0','yellow')]

cuffNorm = pandas.read_table('E_coli_genes.count_table.txt')
f=plt.figure(figsize=(6,6))
f.text(0.5,0.975,'RPKM Comparisons Bicyclomycin Treatments',horizontalalignment='center',verticalalignment='top')

for i,condition_pair in enumerate(condition_pairs):
    FPKM_sample1 = list(cuffNorm[condition_pair[0]])
    FPKM_sample2 = list(cuffNorm[condition_pair[1]])
    plt.subplot(2,2,i+1)
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.5, hspace=0.5)
    plt.scatter(FPKM_sample1,FPKM_sample2,c=condition_pair[2],alpha=0.2)
    frame = plt.gca()
    frame.axes.set_xscale('log')
    frame.axes.set_yscale('log')
    plt.xlim(1,1000000)
    plt.ylim(1,1000000)
    #frame.axes.get_xaxis().set_ticks(range(0,10,1))
    #frame.axes.get_yaxis().set_ticks(range(0,10,1))
    frame.axes.set_xlabel(condition_pair[0].rsplit('_',1)[0])
    frame.axes.set_ylabel(condition_pair[1].rsplit('_',1)[0])


plt.show()
#plt.savefig('Pairwise_comparisons.pdf',format='pdf')
'''
#2 reformat cuffnorm tab file to include ratios of FPKMs

cuffDiff_fh = open('E_coli_gene_exp.diff','r')
Diff_heatmap_out = open('HeatMap_Diff.txt','w')

gene_dict = {}
header = cuffDiff_fh.readline()

for line in cuffDiff_fh:
    line = line.strip().split('\t')
    gene= line[2]
    sample1 = line[4]
    sample2 = line[5]
    status = line[6]
    value1 = line[9]
    if value1 == 'inf': value1 = 10
    if value1 == '-inf': value1 = -10
    if sample1 =='control_20min' and (sample2=='20bicyclomycin_20min' or sample2=='100bicyclomycin_20min'):
            if status == 'NOTEST':
                gene_dict[gene]='fail'
                continue
            if gene not in gene_dict:
                gene_dict[gene] = []
            if gene_dict[gene] != 'fail':
                gene_dict[gene].append(value1)


Diff_heatmap_out.writelines("\t".join(['gene','20MG/CTRL','100MG/CTRL','\n']))
print len(gene_dict)

for gene in gene_dict:
    if gene_dict[gene] != 'fail':
        Diff_heatmap_out.writelines("%s\t%s\t%s\n"%(gene,str(gene_dict[gene][0]),str(gene_dict[gene][1])))






